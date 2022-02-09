#!/usr/bin/env python
# coding: utf-8

# # Chapter 5: Conductance Based Models
# 
# ```{caution} This book was initially prepared on short notice and is an ongoing, ever-evolving project. Many of the ideas, simulations, and visualizations here are incomplete, and most are missing citations. If you feel that I have neglected to cite the proper sources, please do not be offended. It is more than likely that I am in the processes of adding the relevant citations.
# ```

# In[1]:


# Scientific computing
import pandas as pd
import numpy as np

# Web friendly plotting with Bokeh
from bokeh.models import ColorBar, ColumnDataSource, Title, BoxAnnotation, Span, Legend, LabelSet, CategoricalColorMapper
from bokeh.palettes import Viridis256, Magma256, Turbo256, Cividis256, Colorblind
from bokeh.plotting import figure, output_file, show
from bokeh.transform import linear_cmap, cumsum, CumSum
from bokeh.layouts import row, gridplot, layout
import bokeh.io
bokeh.io.output_notebook()

# Matplotlib, for when Bokeh fails
import matplotlib.pyplot as plt
from matplotlib import ticker


# In[2]:


from IPython.display import YouTubeVideo


# ```{toggle}
# $$
# \require{color}
# % Colorblind pallette
# \definecolor{Indigo}{RGB}{51, 34, 136}
# \definecolor{Cyan}{RGB}{136, 204, 238}
# \definecolor{Teal}{RGB}{68, 170, 153}
# \definecolor{Green}{RGB}{17, 119, 51}
# \definecolor{Olive}{RGB}{153, 153, 51}
# \definecolor{Sand}{RGB}{221, 204, 119}
# \definecolor{Rose}{RGB}{204, 102, 119}
# \definecolor{Wine}{RGB}{136, 34, 85}
# \definecolor{Purple}{RGB}{170, 68, 153}
# $$
# ```

# ## The Point Neuron vs. Multi-Compartment Models
# 
# Let's recall the complexity of neuronal morphology. Many neurons have dendritic trees and axons with many branches. Though it is possible to construct neuron models that take this complexity into account, we will not be doing so in this course since these models are high dimensional, and with high dimensional models we lose many of the visual tools available to us for making sense of dynamical systms. The general approach to biologically realistic neuron models is to break up the neuron (cell body, dendrites, axon) into many little compartments (hence why these models are called *multi-comparment* models), each with its own distribution of ion channels. The ionic currents within these compartments and the currents flowing between compartments (treated as electrical synapses) are then studied. In this chapter, we will be focusing on *point neuron* models, or models with a single compartment lumping the soma, dendrites, and axon together.
# 
# ```{figure} multi_comp.png
# :name: multi_comp
# 
# (A) A drawing of a real neuron. (B) The same neuron abstracted into multiple compartments. In a dynamical model, each compartment would have its own membrane potential and set of ionic currents, and the current between each compartment would be modeled as an electrical synapse, as in (D) where we see that we can conceive of each compartment as a single point neuron, and connections between compartments as gap junctions between point neurons. In (C), we see a two compartment model where only the soma and dendritic tree are taken into consideration.
# ```
# 
# ## RC Circuits and The Passive Neuron
# 
# Just as fixed point dynamics are the simplest behavior a dynamical system can exhibit, the simplest model of a neuron is one that exhibits only fixed point dynamics. Imagine a neuron with no active conductances, only a single passive one that is not sensitive to voltage or any other variable. In electrophysiology, *active* and *passive* have different meanings than they do in electrical circuit terminology. By *active conductance*, we just mean an element of the cell that conducts ions across the membrane and is sensitive to some variable such as the membrane potential. Any conductance that is not sensitive to some cellular variable is *passive*. 
# 
# A passive conductance will typically have its own corresponding reversal potential and is often referred to as a *leak channel* since current "leaks" out of it passively. We can model leak currents as Ohmic currents:
# 
# $$ I_{leak} = g_{leak} \left [V_m - E_{leak} \right ] $$
# 
# Such leak channels are usually used to account for unidentified current sources in a neuron. We can model a neuron having only a single passive conductance as resistor-capacitor (RC) circuit. 
# 
# How should we model such as passive neuron? Recall the capacitor equation from the second chapter:
# 
# $$ C_m V_m = Q_m $$
# 
# where $Q_m$ is the total charge built up on either side of the membrane, $C_m$ is the membrane capacitance, and $V_m$ is the membrane potential. Just as Newton's second law gives us a law describing how an object's velocity changes, we need a law that tells us how the membrane potential of a neuron changes. The capacitor equation provides us with a way to such a law. Since we are interested in how the membrane potential changes in time, lets take the time derivative of the capacitor equation:
# 
# $$ \frac{d}{dt} \left [ C_m V_m \right ] = C_m \frac{dV_m}{dt} = \frac{dQ_m}{dt} $$
# 
# The time derivative of the charge is just the total ionic current across the membrane, $I_m$. The total current across the membrane is just the sum of the all the ionic currents in the cell:
# 
# $$ I_m = \sum_j I_j(x_1, x_2, ... , x_n) = \sum_j g_j(x_1, x_2, ... , x_n) \left [V_m - E_j \right ]$$
# 
# The total current across the membrane in this case is just the current from the leak channel plus any current we might want to inject into the cell with an electrode, so adopting the dot notation for time derivatives ($\dot{x} = dx/dt$), we can write the passive neuron model as follows:
# 
# $$ C_m \dot{V}_m = g_{leak} \left [V_m - E_{leak} \right ] + I_{inj}$$
# 
# where $I_{inj}$ refers to the current injected by an electrode. If we inject steps of current into the cell, we can witness the dynamics of the RC circuit comprising the passive neuron. First, the membrane potential of the cell rises exponentially to a steady state voltage $V_{\inf}$. This is an unstable fixed point of the model and the trajectory can only stay here while current is being injected (much in the same way that a pendulum can only stay in the upright position while it is being held there by someone). Second, once we stop injecting current, the membrane potential decays exponentially back to its resting state, the stable fixed point of the system.
# 
# ```{figure} rc_dynamics.jpg
# :name: rc_dynamics
# 
# A diagram illustrating the injected current step (top) and the membrane potential dynamics (bottom) of the passive neuron. The inset equations represent the exponential rise and decay of the voltage. The time constant of the dynamics is $\tau = C_m/g_{leak}$.
# ```
# 
# ## Adding in Active Conductances Yields Excitability
# 
# The fixed-point dynamics of the passive neuron don't give us much insight into the interesting bioelectrical phenomena that have captivated neurophysiologists for centuries. We need models that are capable of reproducing the wide variety of neuronal dynamics observed across the many nervous systems of the animal kingdom. As you know from previous chapters, the missing ingredients in the passive neuron model are ion channels. Specifically, it is voltage-gated ion channels that contribute most to shaping the a neuron's membrane potential dynamics. Though other kinds of ion channels, such as those gated by pressure or neurotransmitters, certainly contribute to the changes in the membrane potential, they generally do so only over slower timescales. Voltage-gated ion channels, on the other hand, can function across the entire spectrum of timescales. Fast variations of ionic currents are what create phenomena like spiking and bursting.
# 
# Recall the formalism introduced in the second chapter for modeling ionic currents $I_j$ where $j$ is a label indicating the species of ion channel:
# 
# $$I_j(x_1, x_2, ... , x_n) = g_j(x_1, x_2, ... , x_n)\left [ V_m - E_j  \right ]$$
# 
# In the next section, we'll focus on the Hodgkin-Huxley formalism for modeling voltage-gated ion channels, that is, ion channels whose conductance depends explicitly *only* on the membrane potential:
# 
# $$I_j(V_m) = g_j(V_m)\left [ V_m - E_j  \right ]$$
# 
# ### Voltage-Gated Ionic Currents the Hodgkin-Huxley Way
# 
# The innovation of Hodgkin and Huxley was to construct a purely functional (as opposed to mechanistic) model of ionic currents that depend on voltage. In the early 1950s, when Hodgkin and Huxley were first attempting to model the action potential, it was hypothesized that the rapid rise in the membrane potential seen during the action potential was due to rapid changes in the membranes permeability to different ions, causing rapid changes in the ionic currents flowing into and out of the membrane. Though we now know that it is ion channel conductivity and not membrane permeability that changes, we can model both possibilities in the same way if we ignore mechanisms and focus on developing a function that tells us how an ionic current depends the membrane potential.
# 
# Hodgkin and Huxleys' approach was to posit that every ionic current has a *maximal conductance* $\overline{g}_j$, with the actual conductance at any given voltage being some fraction of the maximal conductance and varying with the permeability of the membrane to that ion species. They hypothesized that this fraction $p_j$ could be represented as a function of the membrane potential, $p_j(V_m)$. Hodgkin and Huxley didn't know about ion channels when they were coming up with their model, but we now know it is not the permeability of the membrane but the proportion of open ion channels that varies with the voltage. The model for the ionic current would then be
# 
# $$I_j(V_m) = \overline{g}_j p_j(V_m) \left [ V_m - E_j  \right ]$$
# 
# Their next move was to introduce two kinds of variables called *gating variables*. One kind of gating variable, called an *activation gate* and represented by the function $m_j(V_m)$, increases the proportion of *open* ion channels over a range of voltages. The second kind of gating variable, called an *inactivation gate* and represented by the function $h_j(V_m)$, increases the proportion of *closed* ion channels over a range of voltages. Hodgkin and Huxley proposed that the function $p_j(V_m)$ would be some curve dependent on these gating variables:
# 
# $$p_j(V_m) = m_j^p(V_m)h_j^q(V_m)$$
# 
# The exponents $p$ and $q$ arise as follows: Hodgkin and Huxley knew that some chemical reaction was responsible for changing ionic conductivity, and even though they were not aware of ion channels or their biophysics, they conceived of the gating variables as chemical agents in that reaction. From the theory of chemical kinetics, they knew that the combination of sigmoidal and exponential curves they had observed for $p_j(V_m)$ could be fit by adding the exponents $p$ and $q$ as parameters of their model. They ended up with a final model of the ionic current that looks as follows:
# 
# $$I(V_m) = \overline{g}_j m_j^p(V_m)h_j^q(V_m)\left [ V_m - E_j  \right ]$$
# 
# For Hodgkin and Huxley, the exponents $p$ and $q$ were just parameters to help fit the $p_j(V_m)$ curves to experimental data, but we now know that each ion channel species has a certain number of amino acid components that serve as the activation and inactivation gates; the exponent $p$ corresponds to the number of activation gates for each ion channel, while the exponent $q$ corresponds to the number of inactivation gates.
# 
# Recalling our passive neuron model, we can simply sum each of these ionic currents to obtain the total current, giving us a model for how the membrane potential changes in time in the presence of multiple species of ion channels:
# 
# $$ C\dot{V}_m = \sum_j \overline{g}_j m_j^p(V_m)h_j^q(V_m)\left [ V_m - E_j  \right ]$$
# 
# Neuronal models that take this form are referred to as *conductance based models* or *Hodgkin-Huxley models*.
# 
# ```{figure} hh_chan.png
# :name: hh_chan
# 
# An abstract representation of the activation and inactivation mechanisms of a voltage-gated ion channel. As the membrane potential changes, the voltage sensor changes conformation, opening the channel's activation gate. Soon, the inactivation gate moves to plug the open channel and won't be released until the voltage changes again. 
# ```
# 
# ### Excitiability and the Action Potential
# 
# Once you add one or more of these active ionic conductances to a neuron model, you start to get more interesting dynamics. The phenomenon that Hodgkin and Huxley originally set out to model was the action potential. As we have discussed previously, the action potential is a rapid, large deviation of the membrane potential towards more positive (*depolarized*) values, often in response to inputs from other neurons.
# 
# Neurons exhibiting single action potentials in response to stimulation can be modeled as dynamical systems with the property of *excitability*. Excitable dynamical systems are systems with one stable fixed point and a vector field such that for some small neighborhood around the fixed point, there is at least one trajectory starting in that neighborhood which leaves the neighborhood and then returns to the fixed point. This excursion from the neighborhood around the stable fixed point (the "resting state" of the neuron) constitutes an action potential. 
# 
# Notice that we haven't said anything specifically about what the vector field of an excitable system looks like, and this is because there can be a lot of variability in the vector field. The excursion of a trajectory from the neighborhood of the fixed point may be large or small, and there may even be subthreshold oscillations as the trajectory decays back to the fixed point (subthreshold oscillations are much like the decaying oscillations one sees in a damped spring-mass system).
# 
# Excitable systems, having a stable fixed point, are usually found at that fixed point. Therefore, to exhibit excursions away from the fixed point, they must be perturbed by some form of input. That input could be current injected through an electrode or synaptic communication. Normally, once we start thinking about time varying inputs to a system, we have to move into the realm of *non-autonomous* dynamical systems. But in the case of simple step-inputs, we can simplify things by conceiving of such perturbations not as changing the vector field of the system, but merely shifting the initial conditions. So what the inputs do in this case is shift the initial conditions of the system away from the stable fixed point into the neighborhood around it from which it then departs.
# 
# ```{figure} excit.png
# :name: excit
# 
# A diagram illustrating the difference between excitability and oscillatory activity. In the excitable system on the left, trajectories starting in a neighborhood around a stable fixed point make an excursion before returning to the fixed point. On the right, the oscillatory system has a stable limit cycle instead.
# ```
# 
# ## From Excitability to Oscillations: Tonic Spiking and Bursting
# 
# ### A Note on Bifurcations
# 
# We will talk about bifurcations at length in a later chapter, but we need to say a piece about them now so that we can better understand the link between excitability and oscillatory phenomena in neurons. Every dynamical system has parameters of some sort. For example, in the Hodgkin-Huxley models we introduced earlier, the membrane capacitance $C_m$, the reversal potentials $E_j$, and the maximal conductances $\overline{g}_j$ serve as parameters. Parameters are values in a model that don't change in time; once we fix the values of parameters, we have fixed the model. 
# 
# If we change parameters, we alter the vector field associated with the model. We can imagine parameters as dials that we can twist, and as we twist the dials, we change the shape of the vector field and therefore the possible dynamics of the model. In many models, if we change one or more of the parameters enough, we will see a qualitative transformation of the vector field, resulting in a change in the number of equilibria. Any change in one or more parameters of a model leading to a qualitative transformation of the dynamical system's vector field that results in change in the number of equilibria is called a *bifurcation*. For example, a system that loses or gains a fixed point as one of its parameters is varied is undergoing a bifurcation. 
# 
# ```{figure} sn_bifurcation.gif
# :name: sn_bif
# 
# An illustration of a bifurcation in a one-dimensional system. On the horizontal axis is the state of the system, $x$, while on the vertical axis is the time derivative of the system, $v = dx/dt$. As a parameter $\epsilon$ of the system changes, the curve representing the velocity shifts up and down, causing the vector field to change and introducing or removing two fixed points, one stable (red) and the other unstable (green). 
# ```
# 
# It turns out that excitable dynamical systems are systems that are near bifurcations. If we sufficiently alter the parameters of an excitable system, we can cause those systems to undergo bifurcations, resulting in the appearance of new equilibria. In the next couple of sections, we'll be introduced to two neuronal phenomena that depend on bifurcations of excitable systems, *tonic spiking* and *bursting*.
# 
# ### Tonic Spiking
# 
# Tonic spiking is simply the case when the large excursions seen in single action potentials become part of a stable limit cycle. Then the cell will spike repeatedly for an indefinite amount of time. Some excitable systems can undergo a bifurcation that either reveals a new stable limit cycle or stabilizes a previously unstable limit cycle, leading to tonic spiking. Some systems can even exhibit *bistability*, where a stable fixed point coexists with a stable limit cycle, and input to the system can switch the dynamics between the two equilibria.
# 
# 
# ### Bursting
# 
# Bursting is a phenomena in which a neuron releases a finite sequence of spikes called a *burst*, before decaying back to a resting state. Bursting requires multiple bifurcations: first, a bifurcation from the resting state into the spiking state, and then another bifurcation from the spiking state into the resting state. We'll talk in greater depth about bursting when we get into the math of bifurcations. 
# 
# ```{figure} burst_tonic.png
# :name: burst_tonic
# 
# A diagram illustrating different firing patterns of neurons. *Tonic* indicates continuous bursts or spikes, while *phasic* indicates a single burst or spike.
# ```
