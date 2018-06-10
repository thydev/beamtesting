from __future__ import absolute_import

import argparse
import logging
import re

import six

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

options = PipelineOptions()
google_cloud_options = options.view_as(GoogleCloudOptions)
google_cloud_options.project = 'my-project-id'
google_cloud_options.job_name = 'myjob'
google_cloud_options.staging_location = 'gs://agistaging'

google_cloud_options.temp_location = 'gs://agilisium'
options.view_as(StandardOptions).runner = 'DataflowRunner'

p = beam.Pipeline(options=options)
