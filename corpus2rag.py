corpus_of_documents = [
    "A GPU, or Graphics Processing Unit, is specialized hardware used to accelerate the creation of images and videos for output to a display. GPUs are essential for gaming, video editing, and running complex graphic design software.",
    "There are two major brands of GPUs: NVIDIA and AMD. NVIDIA is known for its GeForce series, while AMD markets the Radeon series. Both offer a range of products catering to casual users up to professional graphics developers.",
    "RAM, or Random Access Memory, is a type of computer memory that can be accessed randomly. It is used to store the working data and machine code currently in use. RAM is a critical component for ensuring that a computer can process tasks efficiently.",
    "There are several types of RAM, including DDR4 and DDR5, which stand for 'Double Data Rate 4' and 'Double Data Rate 5', respectively. DDR5 is the latest standard that offers improvements in speed and power efficiency over DDR4.",
    "An SSD, or Solid State Drive, is a type of storage device that uses flash memory to store data persistently. SSDs are faster than traditional HDDs (Hard Disk Drives), making them ideal for rapid boot times and quick file access.",
    "The motherboard is the main circuit board in a computer. It connects all the different components, such as the CPU, GPU, RAM, and storage devices, allowing them to communicate with each other.",
    "A CPU, or Central Processing Unit, is the primary component of a computer that performs most of the processing inside. CPUs run processes and execute instructions that make up computer programs.",
    "Power supplies are crucial for providing power to your PC's components. They convert the AC electricity from your wall outlet into low-voltage DC power for the internal parts of the computer.",
    "A computer case, or chassis, houses all the PC components, protecting them and allowing for airflow to keep the parts cool. Cases come in various sizes and configurations, which can affect the cooling efficiency and noise level.",
    "Cooling systems in a PC, such as fans and liquid cooling solutions, are essential to keep components within safe operating temperatures. Overheating can cause reduced performance or even hardware failure."
]


# Fonction de similarité de Jaccard
def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection) / len(union)

# Fonction pour retourner la meilleure réponse
def return_response(query):
    corpus = corpus_of_documents
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(query, doc)
        similarities.append(similarity)
    return corpus[similarities.index(max(similarities))]
  # Output: Discover the latest electric vehicle with a range of 300 miles on a single charge.