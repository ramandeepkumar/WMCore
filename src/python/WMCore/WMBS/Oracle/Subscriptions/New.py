#!/usr/bin/env python
"""
_Subscription.New_

Oracle implementation of Subscription.New
"""




from WMCore.WMBS.MySQL.Subscriptions.New import New as NewMySQL

class New(NewMySQL):
    """
    Sequence.
    """
    sql = """INSERT INTO wmbs_subscription (id, fileset, workflow, subtype,
                                            split_algo, last_update) 
               SELECT wmbs_subscription_SEQ.nextval, :fileset, :workflow, id,
                      :split_algo, :timestamp FROM wmbs_sub_types
               WHERE name = :subtype""" 
