# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Witness(models.Model):
    _name = 'auth.witness'
    name = fields.Char()
    id_no = fields.Char()


class Sites(models.Model):
    _name = 'auth.sites'

    name = fields.Char()
    courtId = fields.One2many('auth.courts', 'siteId')

class Courts(models.Model):
    _name = 'auth.courts'

    name = fields.Char()
    authorId = fields.One2many('auth.author', 'courtId')
    siteId = fields.Many2one('auth.sites')


class ِِِِِِAuthorِِ(models.Model):
    _name = 'auth.author'

    name = fields.Char()
    courtId = fields.Many2one('auth.courts')
    location = fields.Char(required=True)
    tel = fields.Char()

class MarriageCertificate(models.Model):
    _name = 'auth.cert'
    _description = 'MarriageCertificate'

    name = fields.Char()
    crt_date = fields.Date()
    crt_higri_date = fields.Date()
    authorId = courtId = fields.Many2one('auth.author')
    crt_husband = fields.Char()
    crt_husband_id = fields.Char()
    crt_wife = fields.Char()
    crt_wife_id = fields.Char()
    witnessIds = fields.Many2many("auth.witness", "witnesses", "cert_id", "witness_id")




