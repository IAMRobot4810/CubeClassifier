# Copyright 2018 IAM Robot. All Rights Reserved.
#
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
# ==============================================================================

import cv2
from PIL import Image
from time import sleep
import time
import sys
sys.path.insert(0, './label_image')

import label_image as li

if __name__ == '__main__':
  graph = li.load_graph("quantized_graph.pb")
  while (1 == 1):
    start = time.time()
    img = Image.open('images.jpg')
    result = str(li.classify("images.jpg", graph, "output_labels.txt",
              224, 224, 128, 128, "input", "final_result", True))
    objects = result.split()
    if ("cube" in objects[0]):
      print("Yooo, that's a PowerCube(TM)!")
    else:
      print("Nope, not a PowerCube.")
    stop = time.time()
    print("Classification took " + str(stop-start) + " seconds")

