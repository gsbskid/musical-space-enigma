from unstructured.partition.pdf import partition_pdf

# Returns a List[Element] present in the pages of the parsed pdf document
elements = partition_pdf("sample.pdf")

raw_pdf_elements = partition_pdf(
    filename="sample.pdf",
    extract_images_in_pdf=True,
    infer_table_structure=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    extract_image_block_output_dir='out',
)

# Userfull link  https://github.com/AIAnytime/Multimodal-RAG-using-Langchain/tree/main