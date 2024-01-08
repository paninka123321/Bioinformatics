import pandas as pd

def process_blast_results(blast_results_file):
    # Read BLAST results into a DataFrame
    blast_df = pd.read_csv(blast_results_file, sep='\t', header=None,
                           names=["query", "subject", "identity", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore"])

    # Extract relevant columns
    relevant_cols = ["query", "subject", "identity"]
    blast_df = blast_df[relevant_cols]

    # Pivot the DataFrame to create a similarity matrix
    similarity_matrix = blast_df.pivot(index="query", columns="subject", values="identity").fillna(0)

    return similarity_matrix

# Process BLAST results for each protein
#protein1_similarity = process_blast_results("blast_results_protein.txt")
# Repeat the above line for other proteins

# Save the similarity matrices to files
#protein1_similarity.to_csv("similarity_matrix_protein1.csv")
# Repeat the above line for other proteins
