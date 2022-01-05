import requests
import pytest
import coo_setting


class Interface:
    def __init__(self, path, parameters, summary):
        self.path = path
        self.parameters = parameters
        self.summery = summary

