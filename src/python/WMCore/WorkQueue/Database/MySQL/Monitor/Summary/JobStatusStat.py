"""
WMCore/WorkQueue/Database/MySQL/Monitor/JobStatusStat.py


DAO object for WorkQueue

"""

__all__ = []




from WMCore.Database.DBFormatter import DBFormatter
from WMCore.WorkQueue.Database import States

class JobStatusStat(DBFormatter):
    
    sql = """SELECT status, CAST(SUM(num_jobs) AS UNSIGNED) as jobs  
             FROM wq_element GROUP BY status"""
    
    def convertStatus(self, data):
        """
        Take data and convert status number to string
        TODO: overwrite formatDict to prevent this loop.
        """
        #total = 0
        for item in data:
            item.update(status = States[item['status']])
            #total += item['number']
        
        #for item in data:
        #    item.update(total = total)
        
    def execute(self, conn = None, transaction = False):
        results = self.dbi.processData(self.sql, conn = conn,
                                       transaction = transaction)
        formResults = self.formatDict(results)
        self.convertStatus(formResults)
        return formResults