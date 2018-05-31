#!/usr/bin/env python
# This file is part of the survey_mail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .survey import *

def register():
    Pool.register(
        Survey,
        Configuration,
        ConfigurationSmtp,
        module='survey_mail', type_='model')

