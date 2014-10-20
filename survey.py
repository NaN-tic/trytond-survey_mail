#!/usr/bin/env python
# This file is part of the survey_mail module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval, Bool

__all__ = ['Configuration', 'Survey']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'survey.configuration'
    smtp = fields.Property(fields.Many2One('smtp.server', 'SMTP', required=True))


class Survey:
    __name__ = 'survey.survey'
    send_email = fields.Boolean('Send Email',
        help="Survey data will be send by email")
    email_cc = fields.Char('Email CC',
        states={
            'invisible': ~Bool(Eval('send_email')),
        }, depends=['send_email'],
        help="Emails separated by comma")

