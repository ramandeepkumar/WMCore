#!/usr/bin/env python
"""
_DBS3Buffer.CreateBlocks_

Create new block in dbsbuffer_block

"""

from WMCore.Database.DBFormatter import DBFormatter

class CreateBlocks(DBFormatter):

    def execute(self, blocks, conn = None, transaction = False):

        sql = """INSERT INTO dbsbuffer_block
                 (dataset_id, blockname, location, status, create_time)
                 SELECT (SELECT id from dbsbuffer_dataset WHERE path = :dataset),
                        :block,
                        (SELECT id FROM dbsbuffer_location WHERE se_name = :location),
                        :status,
                        :time
                 FROM DUAL
                 """

        bindVars = []

        for block in blocks:

            bindVars.append( { 'dataset' : block.getDataset(),
                               'block' : block.getName(),
                               'location' : block.getLocation(),
                               'status' : block.status,
                               'time' : block.getStartTime() } )

        self.dbi.processData(sql, bindVars, conn = conn,
                             transaction = transaction)

        return
