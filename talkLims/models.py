__author__ = "Ashok Ragavendran"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "ashok.ragavendran@gmail.com"
__maintainer__ = "Ashok Ragavendran"
__status__ = "Production"

from django.db import models


class ProjectInfo(models.Model):
    project_id = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    project_driver = models.CharField(max_length=100)
    driver_email = models.TextField(null=True)
    request_id = models.CharField(max_length=100)
    expected_completion_date = models.CharField(max_length=100)
    ##project_description = models.TextField(null=True)


class RequestInfo(models.Model):
    protocol_type = models.CharField(max_length=100)
    request_id = models.CharField(max_length=100)
    request_archivist = models.CharField(max_length=100)
    requested_by = models.CharField(max_length=100)
    request_date = models.CharField(max_length=100)
    expected_completion_date = models.CharField(max_length=100)
    quote_number = models.CharField(max_length=100)
    number_of_samples = models.CharField(max_length=100)
    number_of_reads = models.CharField(max_length=100)
    amount_required = models.CharField(max_length=100)
    volume_required = models.CharField(max_length=100)


class TempPullRequest(models.Model):
    request_id = models.CharField(max_length=100)
    scan_id = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)

    location_jane = models.CharField(max_length=100, null=True)
    box_name = models.CharField(max_length=100, null=True)
    shelf_jane = models.CharField(max_length=100, null=True)
    rack_jane = models.CharField(max_length=100, null=True)
    slot_jane = models.CharField(max_length=100, null=True)
    grid = models.CharField(max_length=100, null=True)
    amount_jane = models.CharField(max_length=100, null=True)
    vol_jane = models.CharField(max_length=100, null=True)
    comments_from_request = models.TextField(null=True)


class PullInfo(models.Model):
    request_id = models.CharField(max_length=100)
    ##number_samples = models.CharField(max_length=100)
    ##number_read = models.CharField(max_length=100)
    ##amount_required = models.CharField(max_length=100)
    ##volume_required = models.CharField(max_length=100)
    ##request_date = models.CharField(max_length=100)
    ##expected_completion_date = models.CharField(max_length=100)
    ##protocol_type = models.CharField(max_length=100)
    ##request_archivist = models.CharField(max_length=100)
    ##requested_by = models.CharField(max_length=100)

    ##archivist = models.CharField(max_length=100)
    pull_date = models.CharField(max_length=100)
    assigned_tech = models.CharField(max_length=100)

    barcode_id = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)

    location_jane = models.CharField(max_length=100)
    box_name = models.CharField(max_length=100, null=True)
    shelf_jane = models.CharField(max_length=100)
    rack_jane = models.CharField(max_length=100)
    slot_jane = models.CharField(max_length=100)
    grid_jane = models.CharField(max_length=100)
    amount_jane = models.CharField(max_length=100)
    vol_jane = models.CharField(max_length=100)
    comments_from_request = models.TextField(null=True)

    scan_id = models.CharField(max_length=100)
    location_from_pull = models.CharField(max_length=100)
    box_name_from_pull = models.CharField(max_length=100)
    shelf_from_pull = models.CharField(max_length=100)
    rack_from_pull = models.CharField(max_length=100)
    slot_from_pull = models.CharField(max_length=100)
    grid_from_pull = models.CharField(max_length=100)
    amount_from_pull = models.CharField(max_length=100)
    vol_from_pull = models.CharField(max_length=100)
    comments_for_pull = models.CharField(max_length=100)


class PlateSetup(models.Model):
    request_id = models.CharField(max_length=100, null=True)
    plate_id = models.CharField(max_length=100, null=True)
    plate_name = models.CharField(max_length=100, null=True)
    plate_made_date = models.CharField(max_length=100, null=True)
    agilent_location = models.TextField(null=True)

    well = models.CharField(max_length=100, null=True)
    sample_number = models.IntegerField(null=True)
    barcode_id = models.CharField(max_length=100, null=True)
    scan_id = models.CharField(max_length=100, null=True)
    sample_name = models.CharField(max_length=100, null=True)
    amount_from_plate = models.FloatField(null=True)
    vol_from_plate = models.FloatField(null=True)
    est_dilution = models.FloatField(null=True)  # calculation roundup( conc_from_pull/100)

    dilution_for_agilent = models.FloatField(null=True)
    dil_conc = models.FloatField(null=True)  # calculation roundup( amount_from_pull/ dilution_for_agilent)
    rna_rin = models.FloatField(null=True)
    ribo_28S_16S = models.FloatField(null=True)
    agilent_ng_per_ul = models.FloatField(null=True)
    agilent_corr_ng_per_ul = models.FloatField(null=True)  # Calculation dilution_for_agilent* agilent_ng_per_ul
    conc_to_use = models.FloatField(null=True)
    ul_for_desired_amount = models.FloatField(null=True)  # Calculation 500/ conc_to_use
    water_to_49_ul = models.FloatField(null=True)  # Calculation 49 - ul_to_500_ng
    ercc = models.CharField(max_length=100, null=True)
    comments = models.TextField(null=True)


class LibraryMaking(models.Model):
    plate_id = models.CharField(max_length=100)

    day1_date = models.CharField(max_length=100, null=True)
    day1_comments = models.TextField(null=True)
    day2_date = models.CharField(max_length=100, null=True)
    day2_comments = models.TextField(null=True)
    final_date = models.CharField(max_length=100, null=True)
    final_comments = models.TextField(null=True)

    add_atl = models.TextField(null=True)
    add_lig = models.TextField(null=True)
    add_smm = models.TextField(null=True)
    add_stl = models.TextField(null=True)
    amp_pcr = models.TextField(null=True)
    clean_up_alp = models.TextField(null=True)
    clean_up_pcr = models.TextField(null=True)
    incubate_1_alp = models.TextField(null=True)
    incubate_1_cdp = models.TextField(null=True)
    incubate_1_rbp = models.TextField(null=True)
    incubate_2_alp = models.TextField(null=True)
    incubate_2_cdp = models.TextField(null=True)
    incubate_2_rbp = models.TextField(null=True)
    incubate_rfp = models.TextField(null=True)
    make_cdp = models.TextField(null=True)
    make_pcr = models.TextField(null=True)
    make_rbp = models.TextField(null=True)
    purify_cdp = models.TextField(null=True)
    run_analytical_pcr = models.TextField(null=True)
    step_1_sample_prep = models.TextField(null=True)
    step_2_synthesize_first_strand_dna_50_min = models.TextField(null=True)
    step_3_synthesize_second_strand_dna_and_clean_up_1_hour = models.TextField(null=True)
    step_4_adenylate_3_pr_ends = models.TextField(null=True)
    step_5_enrich_dna_fragments = models.TextField(null=True)
    wash_rbp = models.TextField(null=True)


class LibraryMaking_barcodes(models.Model):
    plate_id = models.CharField(max_length=100)
    plate_sample_number = models.IntegerField(null=True)
    barcode_location = models.CharField(max_length=5)


class Pool(models.Model):
    pool_id = models.CharField(max_length=100)


### Tables Deprecated

class SampleManifest(models.Model):
    sample_id = models.CharField(max_length=100)
    sample_name = models.CharField(max_length=100)
    sample_replicate = models.IntegerField()
    sample_species = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=100)
    sample_conc = models.FloatField(null=True)
    sample_amount = models.FloatField(null=True)
    project_id = models.CharField(max_length=100)
    other = models.TextField()
    desc = models.TextField()
