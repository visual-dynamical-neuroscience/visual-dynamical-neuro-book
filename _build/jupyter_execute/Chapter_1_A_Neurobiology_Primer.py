#!/usr/bin/env python
# coding: utf-8

# # Chapter 1: A Neurobiology Primer
# 
# ```{caution} This book was initially prepared on short notice and is an ongoing, ever-evolving project. Many of the ideas, simulations, and visualizations here are incomplete, and most are missing citations. If you feel that I have neglected to cite the proper sources, please do not be offended. It is more than likely that I am in the processes of adding the relevant citations.
# ```

# In[1]:


from IPython.display import YouTubeVideo


# ## The Facts of the Matter
# 
# Despite wanting to present biology as more than just a stamp collection or list of facts to memorize, we do need a shared vocabulary and set of concepts to work with before we can start doing some modeling. In this section, I hope to provide an engaging overview of a few biological principles that will aid in your understanding of neurobiology. So that you don't get overwhelmed or find yourself asking why you need to know any of this, I have chosen to cover only what you'll need to understand the models we'll be working with while still giving you enough context that you don't feel lost. Unfortunately, this means I'll be glossing over a whole universe of interesting phenomena and processes that are critically important for appreciating and explaining the full complexity of life. Hopefully, there's enough information here for you to fill in the details with your own research. 
# 
# ### Cells
# 
# I will assume that the vast majority of you will at some point have taken a middle school or high school biology class so that I can comfortably use the word "cell" without having to explicitly define it, and you will have some idea of what I am talking about. In what follows, I will in general only cover the properties of animal cells, leaving aside the intricacies of plant and prokaryote cells. As a side note, it may interest you to know that plants and even some single-celled organisms exhibit interesting bioelectric phenomena traditionally studied only in 
# 
# We can characterize biology as the study of organisms, where by organism, I mean any organic, living system capable of maintaining itself as a system. This is a bit of a tricky definition. What does it mean to be living? To maintain oneself? To a first approximation, all I mean is that organisms, when they have access to sufficient resources, can keep themselves alive, that is, separated or otherwise distinguished from their environment. 
# 
# The original organisms, the first to ever appear on Earth, were single cells, and all organisms we know of are constituted by at least one cell. Cells are distinguished from their environment by a membrane made of lipids, molecules with water-attracting (*hydrophilic*) "heads" and water-repelling (*hydrophobic*) "tails". As you will see in more detail below, these hydrophobic tails cluster together with the hydrophilic heads sticking out, forming a bilayer membrane that encloses the interior of the cell, consisting primarily of an aqueous substance called *cytoplasm*.
# 
# Contrary to some of the more boring cartoon models of cells you may have seen in textbooks showing a static and simply organized cell interior, the cytoplasm of the cell is alive with the constant activity of proteins, sugars, and other molecules. Below is an artistic interpretation of this molecular jungle that I think conveys its dynamism:
# 
# ```{figure} cellularlandscape.jpg
# :name: cell_landscape
# 
# An artistic interpretation of the complex molecular landscape inside (top) as well as at the boundary (bottom) of a eukaryotic cell. Made by Evan Ingersoll and Gael McGill at [Digizyme](https://www.digizyme.com/cst_landscapes.html).
# ```
# 
# But if trying to imagine all of that molecular motion from only a still picture is not your cup of tea, here's a narrated version of a wonderful animated video created by Harvard and the Howard Hughes Medical Institute:

# In[2]:


YouTubeVideo("dp6qRNNGPj4", width=800, height=450)


# Within the cytoplasm of the cell are spatially distinct regions called *organelles*, each with a specific function. Organelles refered to as *membrane-bound* maintained separate from the rest of the cytoplasm by their own lipid bilayers, whereas others, called *non-membrane bound*, are merely large assemblies of macromolecules. I won't provide a detailed list of known organelles and their functions, but it suffices to say that organelles facilitate a diverse set of processes, from protein synthesis and modification to the production of energy for the cell. 
# 
# When first learning cell biology, one is presented with a plethora of chemical reactions and pathways necessary for sustaining the life of the cell. One thing that always confused me was, how do the various molecules involved in these reactions come into contact with each other? Often, molecules must diffuse slowly through the cytoplasm, relying on chance encounters with other molecules that they will react with. A computer simulation of this diffusion process for a protein and sugar molecule is shown below:
# 
# ```{figure} diffusion.jpg
# :name: diffusion
# 
# A computer simulation of the random paths taken by a protein (blue) and sugar (red) molecule diffusing inside a bacterial cell. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/).
# ```
# 
# The dynamism of the cell is not relegated to its interior. The exterior of the cell membrane and the space around it form a three-dimensional network called the *extracellular matrix* consisting of macromolecules and minerals. In addition to providing structural support to cells, this network also governs cell adhesion and cell-to-cell communication. The extracellular matrix is in constant motion, as exhibited by molecular entities such as *lipid rafts* which float along the surface of the cell membrane. 
# 
# ```{figure} ecmatrix.jpg
# :name: ec_matrix
# 
# An artistic interpretation of the extracellular matrix. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/).
# ```
# 
# ### Biological Macromolecules
# 
# We can quickly compile a useful shared vocabulary for talking about cell biology by looking at the large ("macro-") molecules found in cells. We will focus on those macromolecules with identifiable functional roles in the self-maintenance of the cell. 
# 
# #### Carbohydrates
# 
# Carbohydrates are molecules containing carbon (hence the prefix "carbo-"), hydrogen (hence the suffix "-hydrate"), and oxygen in a 1:2:1 ratio. Perhaps the most important function of carbohydrates in cells is their role in cellular metabolism: *monosaccharides* (simple sugars) such as glucose are transformed by the cell into other molecules including *adenosine triphosphate*, a molecule that acts as an energy source for cells by facilitating numerous chemical reactions that are essential for life. Carbohydrates, in the form of glycolipids and glycoproteins, also play numerous other functional roles in the cell, such as stabilizing the structure of the cell membrane and communication between cells. 
# 
# #### Lipids
# 
# Though there are many different categories of lipids, we can characterize lipids broadly as small nonpolar hydrophobic hydrocarbons. That's a mouthful! Roughly, this just means that lipids are made of the elements carbon and hydrogen (hence "hydrocarbons"), repel water (hence "hydrophobic"), and have all electric charges evenly distributed across the molecule so that no electric poles form (hence "nonpolar"). 
# 
# Lipids play several important roles in the life of the cell, such as energy storage and cell signaling (the ability of a cell to receive, process and transmit signals with its environment and with itself), and as we already discussed, lipids are the primary constituents of the cell membrane. The lipids forming the cell membrane are *phospholipids*, lipid molecules with a hydrophilic head containing phosphate and two hydrophobic tails. Phosopholipids in a solution can spontaneously aggregate into interesting structures such as bilayer sheets, spherical monolayers called *micelles*, and spherical bilayers called *liposomes*. Such phospholipid structures likely played an important role in the origin of life on Earth.
# 
# ```{figure} lipid_full.png
# :name: lipid
# 
# (A) An illustration of the structure of phospholipids, showing their hydrophilic heads and hydrophobic tails, as well as a spherical aggregation of lipids. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/). (B) 3D models of some of the aggregate structures that can be formed by lipids in solution. Taken from [Bitounis et al., 2012](https://pubmed.ncbi.nlm.nih.gov/22474607/).
# ```
# 
# #### Proteins
# 
# Proteins are perhaps the most important class of macromolecules in the cell, performing a wide array of functions such as structural support and catalyzing reactions. As we'll see in the next chapter, a special class of proteins known as *ion channels* play a crucial role in governing the electrical properties of neurons, the cells of the nervous system.
# 
# The chemical structure of proteins is complex. The building blocks of proteins are amino acids, molecules with a central carbon atom off of which branch several chemical groups. Different amino acids are distinguished from each other by one chemical group in particular, called the *R group*.  
# 
# The functions of proteins are largely determined by their geometry which has four levels of organization: the primary, secondary, tertiary, and quaternary levels. The primary structure of a protein is the linear chain of amino acids forming the protein, called a *polypeptide*. The secondary structure consists in the local folding of the chain into helices and pleated sheets. The tertiary structure of proteins is the overall three-dimensional structure that sequence of helices and sheets folds into. Sometimes, two or more polypeptides may come together to form the protein, and their configuration constitutes the quaternary structure of the protein. The structure (and therefore function) of proteins is highly context dependent, being impacted by temperature, pH, as well as the assistance of protein helpers called *chaperones*.
# 
# The amino acids forming the polypeptide chains of proteins are synthesized by organelles called ribosomes based on sequences of nucleic acids known as messenger ribonucleic acids (mRNAs). In the next section, we'll cover the structure and function of these mRNAs along with other nucelic acids.
# 
# ```{figure} protein.jpg
# :name: protein
# 
# An illustration of a possible primary structure for a protein, showing all the common amino acids, as well as a potential tertiary structure resulting from the polypeptide. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/).
# ```
# 
# ```{figure} protein2.jpg
# :name: protein2
# 
# An illustration of the structural hierarchy of proteins. Taken from the [LibreTexts Biology textbook](https://bio.libretexts.org/Bookshelves/Introductory_and_General_Biology/Book%3A_General_Biology_(OpenStax)/1%3A_The_Chemistry_of_Life/3%3A_Biological_Macromolecules/3.4%3A_Proteins).
# ```
# 
# #### Nucleic Acids
# 
# Nucleic acids are large molecules made of smaller molecules called nucleotides, each nucleotide being made of a five-carbon sugar, a nitrogen containing chemical group, and a phosphate group. Different nucleotides differ in the nitrogrenous bases and/or the sugar molecules constituting them. For example, deoxyribose nucleic acid (DNA) contains a different sugar than ribose nucleic acid (RNA). 
# 
# The chemical structure of nucleotides dictate which nucleotides can bond to each other. These bond constraints result in DNA taking on the form of a double helix, where each strand of the helix is bonded to the other via bonds between individual nucleotides forming a chain along the backbone of the helix. Though we wont go into detail about these processes, the fact that each strand is complementary to the other has important implications for the replication and repair of DNA as well as its transcription into messenger RNA. Unlike DNA, RNA is always single stranded, though these single strands may fold back on themselves to create interesting shapes with important functional properties. Though RNA can be found in many forms throughout the cytoplasm, DNA is generally constrained to stay within a protective organelle called the *nucleus*.
# 
# Nucleic acids are often lauded as the most important macromolecules because DNA is said to "encode" proteins in the form of genes, specific sequences of nucleotides that can then be transcribed into mRNA molecules having a complementary sequence, each of which can then be translated by ribosomes (made partly of *ribosomal RNA*) into the sequences of amino acids (carried to the site of protein synthesis by *transfer RNAs*) that form the primary structure of proteins. 
# 
# ```{figure} dna1.jpg
# :name: dna1
# 
# The chemical structure of the DNA double helix illustrating the different types of nucleotides. The double helix splits into a single helix at the top to show a possible structure for RNA. Thymine is a nucleotide unique to DNA, while uracil is unique to RNA. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/).
# ```
# 
# ```{figure} dna2.jpg
# :name: dna2
# 
# An illustration of the bonds between nucleotides in DNA. Taken from [David Goodsell's *The Machinery of Life*](https://ccsb.scripps.edu/goodsell/machinery-of-life-reducedillustrations/).
# ```
# 
# It is common to hear about the *central dogma of molecular biology*, the principle that information only flows in one direction, from DNA to RNA to protein. We know now that this view is extremely flawed. There exist many overlapping and interacting *gene regulatory networks*, collections of molecules that interact with each other and other substances in the cell to regulate gene expression levels of mRNA and proteins. Gene regulatory networks exhibit many feedback interactions in which proteins can modify their own expression or the expression of other proteins in the cell.
# 
# ## What is Life?
# 
# You may be wondering how we are going to address such a vast question in what is meant to be a short primer on the biology of the nervous system. The short answer is that we have no hope of doing so. The longer answer is that even though we cannot provide a comprehensive account of life and all its varied manifestations, This is, after all, a course on theoretical neurobiology, and to simply give a list of known facts about the living world would be antithetical to the aims and spirit of the course. We'll frame our short investigation into the nature of life around a discussion of the dominant metaphor for living systems in the scientific literature, the machine metaphor. Under this metaphor, living organisms are conceived of as just another kind of machine. Our task will be to investigate how well this metaphor matches up with what we know about living systems, and in the course of this investigation hopefully get a few insights into the nature of life. 
# 
# ### Are Cells Machines?
# 
# This is the question asked by philosopher Dan Nicholson in [a recent paper in the Journal of Theoretical Biology](https://philpapers.org/archive/NICITC.pdf). Below, we'll see what Nicholson has to say about what he calls the "machine conception of the cell" before digging into his critique of the machine metaphor.
# 
# #### The Machine Conception of the Cell
# 
# In a video by biologist Johannes Jaeger analyzing Nicholson's paper, Jaeger identifies four properties of machines necessary for understanding the machine conception of the cell:
# 
# 1. **Mechanistic decomposition:** Description in terms of a list of parts and how they fit together.
# 
# 2. **Machine design (prediction and control):** The operations of a machine are tightly constrained by its function.
# 
# 3. **Robustness / reliability:** Machines are highly efficient at what they do (always follow the same sequence of steps in every cycle of their operation)
# 
# 4. **Modularity:** The operation of a machine is not continuous: we can interrupt it to examine machine parts without jeopardising structural integrity.
# 
# With these four properties in mind, many have looked at individual parts and processes within cells exhibiting a machine-like quality, such as [flagellar motors in bacteria](https://youtu.be/cwDRZGj2nnY), and concluded that cells (and therefore life at other scales) must be machines. This metaphor of cells as machines has only been strengthened in the last few decades by increasing use of "information processing" and other computational metaphors to describe the function of genes and cell signaling. In the next section, we'll see why these metaphors may be facile in light of what we know about cell biology.
# 
# #### Cells Are Not Machines
# 
# Crucial to Nicholson's critique of the machine metaphor are the concepts of self-organization and thermodynamic equilibrium. Self-organization is often confused with self-assembly, and by demonstrating the difference between the two concepts, we can also understand the notion of thermodynamic equilibrium. 
# 
# We'll start our analysis of the difference between self-assembly and self-organization by giving definitions for each:
# 
# ```{admonition} Self-Assembly
# The physical association of molecules into a static equilibrium structure without the input of an external energy source.
# ```
# 
# ```{admonition} Self-Organization
# The collective behavior of non-linearly interacting molecules generating a far from equilibrium dissipative structure. By *dissipative*, we just mean that the system is open, exchanging energy and matter with the environment. 
# ```
# To really understand these definitions, we need to know a bit more about thermodynamic equilibrium. We're all familiar with the concept at an intuitive level: take a cup of hot coffee or tea and leave it sitting for a while, and later when you return it will be the same temperature as the room in which you left it. The liquid has reached thermodynamic equilibrium with its surroundings. Imagine that every state $x$ of a system has an associated energy $U(x)$. If we assign a coordinate to each variable of the state, we can picture the *state-space* of the system as a landscape in which the elevation at any state $x$ is determined by the energy associated with that state, $U(x)$. We can imagine the system evolving in time as a ball rolling around this state-space, from one state to the next. Then thermodynamic equilibrium is achieved when the ball rolls into one of the troughs. In this metaphor, since balls tend to roll downhill, the system is guaranteed to reach thermodynamic equilibrium and stay there without some external input of energy to the system. Therefore, we say that those equilibrium states are *stable*, while other states are *unstable*. If, for example, there is a shallow part of the state-space where the elevation of the energy landscape is not much higher than the local minimum, the system may take a while to reach a stable state. We call such regions of the energy landscape *metastable*. Living organisms, cells included, are able to maintain themselves in states far from equilibrium by constantly exchanging matter and energy with their environment. 
# 
# ```{figure} landscape.jpg
# :name: landscape
# 
# ```
# 
# The concept of self-assembly was initially developed to describe how the components of viral capsids (the protein shell of a virus that encloses its genetic material) become assembled into a complete capsid. You can see a video modeling the process of capsid self-assembly below that illustrates the concept:

# In[3]:


YouTubeVideo("X-8MP7g8XOE", width=800, height=450)


# To illustrate the concept of self-organization, take a look at the video below. The video is an animation of cellular cytoskeleton dynamics. The cytoskeleton is a complex, dynamic network of various interlinking protein filaments that rapidly assemble and disassemble to endowing the cell with structure, reistance to mechanical deformation, and motion through its environment.

# In[4]:


YouTubeVideo("tO-W8mvBa78", width=800, height=450)


# Notice the difference between the two examples: whereas the viral capsid assembles itself into a stable state once and remains there, the cytoskeleton constantly assembles and disassembles itself into sequences of metastable states determined by its coupling to the internal and external environments of the cell. The components of the viral capsid, though individually out of thermodynamic equilibrium, eventually reach thermodynamic equilibrium when they come together to form the capsid. The components of the cytoskeleton, on the other hand, are constantly out of thermodynamic equilibrium, never remaining in one state for too long as they respond to environmental perturbations. Now that we (hopefully) have at least a rough idea of the concepts of self-organization and thermodynamic equilibrium, we can move on to understanding why cells (and all organisms) are not machines. 
# 
# Machines almost always exist at or are approaching thermodynamic equilibrium with their surroundings, and must be designed, constructed, and maintained by someone external to the machine. In contrast, cells (and organisms more generally), are self-organizing systems that maintain themselves in states far from thermodynamic equilibrium by continuously exchanging matter and energy with their surroundings. 
# 
# 1. **Emergent mechanics:** No predetermined blueprint or design, but self-organization.
# 
# As we've already seen with the example of the cytoskeleton, cells are constantly restructuring themselves and responding to different environmental contexts, that is, they are self-organizing. The dynamic structure of the cell is not encoded in the genome and DNA is not some instruction manual that directs cellular processes from one moment to the next. Complex gene regulatory networks composed of DNA, RNA, proteins, and other molecules determine gene expression levels. These molecular networks are constantly being modulated by each other and the environment in which they interact. Not only do these gene regulatory networks contribute to the overall state of the cell, they are themselves modulated by the cellular state. Changes in cell state may sometimes be anticipated by the cell, but they can never be known with certainty before they occur, so in what sense could cellular processes be algorithmic or predetermined?
# 
# 2. **Multi-functionality:** The cell's operation is tightly constrained by structure and specificity of its parts.
# 
# 
# 3. **Context dependence:** The cell's operations do not follow any predefined sequences of steps.
# 
# 4. **Holism:** Cells cannot be broken down into parts without jeopardising structural integrity.
# 
# Cells are pretty robust. You can perturb them significantly without destroying them. Raise the temperature, poke them a bit, even swap nuclei between different cells. They'll do fine. But if you try to break the cell down and separate it into its constituent parts (it is empirically possible), you will almost certainly not be able to put it back together again and hope for it to function. Unlike a car, which you can take apart and put back together and drive again, removing the parts of the cell from their processes of interaction is fatal to the cell.  
# 
# Hopefully I've been able to convince you that cells are not machines, and that if they or some of their parts sometimes resemble machines, that resemblance depends on a rich history and ongoing network of interacting processes that are certainly not machine-like. If you are interested in the aforementioned video by Johannes Jaeger covering Dan Nicholson's paper on the machine metaphor of the cell, you can find it below:

# In[5]:


YouTubeVideo("XioauUQxW84", width=800, height=450)


# ### Nervous Systems
# 
# Now that we have a basic understanding of cell biology and the phenomenon of life, we can move on to a few aspects of cell biology that are specific to nervous systems. We'll start out by taking a look at a few of the different cell types found in nervous systems.
# 
# The cells of the nervous system can be broken up into two broad classes: *neurons* and *glia*. Neurons usually get most of the attention, but this has begun to change in recent years with our increasing understanding of glial processes. 
# 
# #### Neurons
# 
# What distinguishes neurons from other cells of the body? One could start with their morphology or with their physiology, but in reality, there is no way to cleanly separate the two aspects of the cell. For neurons especially, their morphology and physiology are intimately related. So we must approach both aspects simultaneously.
# 
# The most defining feature of neurons is that they conduct electricity. Electricity is not unique to neurons, all cells of the body have mechanisms to allow ions (atoms carrying an electrical charge) to pass from one side of the membrane to the other, and therefore exhibit some measure of electrical activity. But what is unique about neurons is that, with a few exceptions, they are the only cells in the body to *actively* conduct electricity, that is, to dynamically alter the way in which ions pass across their membrane over very short time scales (milliseconds). Neurons typically exhibit these rapid changes in conductance in response to stimulation from their environment, a property known as *excitability*. I want these notes to be accessible to as broad an audience as is possible, so I won't go into too much detail here about the electrical properties of neurons. In the next chapter, we will cover the basic physics of electricity before discussing bioelectricity in depth. 
# 
# The morphology of neurons shapes the way they conduct electricity and respond to stimuli. Despite great variability in size and shape, the morphological features of neurons can be roughly broken down as follows:
# 
# * The *soma* is the cell body of the neuron, containing the nucleus.
# * The *dendrites* are tree-like extensions of the cell membrane. Neurons receive the majority of their inputs from other neurons here via nodules called *dendritic spines*.
# * The *axon* is thin, cable-like projection of the cell membrane that may extend long distances from the soma, depending on the neuron type. The function of the axon is to carry electrical signals away from the soma. Axons meet the soma at a region called the *axon hillock*, the electrical properties of which shape the electrical signals traveling down the axon. Axons may have many branches, enabling communication with many other cells simultaneously. Some axons are coated in sleeves of fatty tissue called *myelin* which allows electrical signals to be conducted at faster rates for longer distances.
# * The *axon terminal* is found at the ends of the axonal branches, and often takes the form of *synaptic boutons*, structures specialized for translating electrical signals to chemical signals for interaction between neurons.
# * Regions where one neuron sends signals to another via *neurotransmitter* and *neuromodulator* molecules are called *synapses*. Synapses often take the form of a junction between axon terminals and dendritic spines, though axons may synapse with other neurons on almost any part of the cell, and synapses between dendrites have been observed. In addition to chemical synapses, sometimes neurons may form *gap junctions*, often called *electrical synapses*, with other cells allowing direct transmission of ions between neurons.
# 
# One often sees cartoon models such as the one below illustrating key parts of neuronal anatomy as if they were the same across all neurons:
# 
# ```{figure} model_neuron.png
# :name: model_neuron
# 
# ```
# 
# Nothing could be further from the truth. Though most neurons do share these anatomical features, there is not just one kind of neuron; rather, there are many different types of neurons distributed across different regions of the nervous system that may be distinguished based on their morphology, electrical properties, and gene expression profiles. As illustrated in the figure below, the morphology of these different cell types can vary significantly: 
# 
# ```{figure} neuron_diversity.png
# :name: diversity
# 
# ```
#  
# 
# #### Glia
# 
# Several classes of glial cells exist, each with their own diverse functions. It would be beyond the scope of these notes to enumerate all of these types and their specific details of their functions within the nervous system, so we will focus broadly on the recognized functions of glial cells.
# 
# Glia have been traditionally cast as mere support systems for neurons, providing physical support, nutrients, and immunological protection for neurons. Indeed, some of their primary roles are to repair damaged neurons and prevent toxic build up of neurotransmitters around synapses. Their role in forming myelin sheaths around axons and therefore in shaping electrical signal transmission has long been recognized, but it was believed that otherwise, glia did not contributed to the electrical state of the nervous system.
# 
# This picture has begun to shift in recent years. As it turns out, glia are capable of responding to stimulation by releasing chemicals similar to neurotransmitters and can actively conduct ions in a similar manner to neurons, thereby shaping the electrical state of the nervous system. Additionally, glia guide the development of the nervous system, playing crucial roles in the formation and modification of synapses between neurons as well as guiding neuronal migration during early development.

# In the next chapter, we'll take a deep dive into the electrical properties of neurons and begin to think about how to model them mathematically.
