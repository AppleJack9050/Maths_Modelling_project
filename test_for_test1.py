from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import app
from absl import flags
from absl import logging

from gfootball.env import config
from gfootball.env import football_env
from test import main

if __name__ == '__main__':
    app.run(main)