import io
import unittest

import pyrodigal
from pyrodigal.tests import fasta

import pyrodigal_rv

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files


class TestViralGeneFinder(unittest.TestCase):

    def test_tymoviridae_genome(self):
        gene_finder = pyrodigal_rv.ViralGeneFinder(meta=True)
        with resource_files(__package__).joinpath("Tymoviridae.fna").open("r") as f:
            record = next(fasta.parse(f))
            genes = gene_finder.find_genes(record.seq)
        self.assertIs(genes.metagenomic_bin, pyrodigal_rv.METAGENOMIC_BINS[0])
        with resource_files(__package__).joinpath("Tymoviridae.faa").open("r") as f:
            for gene, protein in zip(genes, fasta.parse(f)):
                self.assertEqual(gene.translate(), protein.seq)

    def test_duamitovirus_genome(self):
        gene_finder = pyrodigal_rv.ViralGeneFinder(meta=True)
        with resource_files(__package__).joinpath("Duamitovirus.fna").open("r") as f:
            record = next(fasta.parse(f))
            genes = gene_finder.find_genes(record.seq)
        self.assertIs(genes.metagenomic_bin, pyrodigal_rv.METAGENOMIC_BINS[62])
        with resource_files(__package__).joinpath("Duamitovirus.faa").open("r") as f:
            for gene, protein in zip(genes, fasta.parse(f)):
                self.assertEqual(gene.translate(), protein.seq)

    def test_atkinsviridae_genome(self):
        gene_finder = pyrodigal_rv.ViralGeneFinder(meta=True)
        with resource_files(__package__).joinpath("Atkinsviridae.fna").open("r") as f:
            record = next(fasta.parse(f))
            genes = gene_finder.find_genes(record.seq)
        self.assertIs(genes.metagenomic_bin, pyrodigal_rv.METAGENOMIC_BINS[3])
        with resource_files(__package__).joinpath("Atkinsviridae.faa").open("r") as f:
            for gene, protein in zip(genes, fasta.parse(f)):
                self.assertEqual(gene.translate(), protein.seq)
