from pyranges1.readers import parse_kv_fields


def test_parse_kv_fields():
    line = (
        'gene_id "PYGB"; transcript_id ""; db_xref "CGNC:51447"; '
        'db_xref "GeneID:421248"; description "phosphorylase, glycogen; brain"; '
        'gbkey "Gene"; gene "PYGB"; gene_biotype "protein_coding";'
    )

    assert parse_kv_fields(line) == [
        ("gene_id", "PYGB"),
        ("transcript_id", "NA"),
        ("db_xref", "CGNC:51447"),
        ("db_xref", "GeneID:421248"),
        ("description", "phosphorylase, glycogen; brain"),
        ("gbkey", "Gene"),
        ("gene", "PYGB"),
        ("gene_biotype", "protein_coding"),
    ]
