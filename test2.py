# coding=utf-8
# Copyright 2019 Google LLC
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Script allowing to play the game by multiple players."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import logging

from gfootball.env import config
from gfootball.env import football_env

def res():
    render = False
    level = '11_vs_11_easy_stochastic'

    cfg_values = {'action_set': 'full', 'dump_full_episodes': True, 'players': '', 'real_time': False,
                  'level': '11_vs_11_easy_stochastic'}

    cfg = config.Config(cfg_values)
    env = football_env.FootballEnv(cfg)
    if render:
        env.render()
    steps = 0
    env.reset()
    try:
        while True:
            obs, rew, done, info, team1_score, team2_score = env.step([])
            steps += 1
            if steps % 100 == 0:
                print("Step %d Reward: %f" % (steps, rew))
            if done:
                print("The final score is %d : %d" % (team1_score, team2_score))
                break
    except KeyboardInterrupt:
        logging.warning('Game stopped, writing dump...')
        env.write_dump('shutdown')
        exit(1)

    return team1_score, team2_score


if __name__ == '__main__':
    a = res()
    print("The final score is %d : %d" % (a[0], a[1]))
