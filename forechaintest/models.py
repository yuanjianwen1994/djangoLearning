# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BlockchainUser(models.Model):
    address = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'blockchain_user'


class Contract(models.Model):
    address = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    abi = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'contract'


class Nft(models.Model):
    full_name = models.CharField(max_length=255)
    contract_address = models.CharField(primary_key=True, max_length=255)
    abi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nft'


class Token(models.Model):
    contract = models.ForeignKey(Nft, models.DO_NOTHING, db_column='contract')
    token_id = models.CharField(max_length=110)

    class Meta:
        managed = False
        db_table = 'token'
        unique_together = (('contract', 'token_id'),)


class Transaction(models.Model):
    hash = models.CharField(max_length=255)
    out_address = models.ForeignKey(BlockchainUser, models.DO_NOTHING, db_column='out_address', related_name='out_address')
    in_address = models.ForeignKey(BlockchainUser, models.DO_NOTHING, db_column='in_address', related_name='in_address')
    token = models.ForeignKey(Token, models.DO_NOTHING)
    quantity = models.IntegerField()
    time = models.DateTimeField()
    token_price = models.FloatField()
    contract = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'transaction'
        unique_together = (('hash', 'in_address', 'out_address', 'time', 'token', 'quantity'),)
