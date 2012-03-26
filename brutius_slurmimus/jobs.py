#!/usr/bin/env python
""" Et tu, brute?  Parsing slurm info the `wrong way`.

This module tries to duplicate some of the functionality of pyslurm but by
instead running slurm commands (squeue, sinfo) and parsing their output.

Its no cross platform, or secure, or anything.  Its a standin until pyslurm
supports the 2.2.7 API.

"""

import os


def slurm_load_jobs():
    columns = [
        'jobid', 'partition', 'name', 'user',
        'st', 'time', 'nodes', 'nodelist',
    ]
    cmd = 'squeue'
    output = os.popen(cmd).readlines()
    jobs = [dict(zip(columns, line.split())) for line in output[1:]]
    return jobs

def slurm_load_job_details(jobid):
    cmd = 'scontrol show job %r' % jobid
    output = ' '.join(os.popen(cmd).readlines())
    items = output.split()
    pairs = [tuple(item.split('=')) for item in items]
    pairs = [pair for pair in pairs if len(pair) == 2]
    job = dict(pairs)
    return job



if __name__ == '__main__':
    jobs = slurm_load_jobs()
    job = slurm_load_job_details(jobs[0]['jobid'])
    import pprint
    pprint.pprint(job)
