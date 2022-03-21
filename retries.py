"""
Configuration for retry_if_did_not_produce_data function
"""


def retry_if_did_not_produce_data(result):
    """Function trigers retries when decorated finction returns 'False'"""
    return result is False
