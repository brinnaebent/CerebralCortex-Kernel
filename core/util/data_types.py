# Copyright (c) 2017, MD2K Center of Excellence
# - Nasir Ali <nasir.ali08@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import json


def convert_sample(sample):
    if isinstance(sample, str) and "\x00" in sample:
        sample = sample.replace("\x00", "")

    if isinstance(sample, tuple):
        values = list(sample)
    elif isinstance(sample, list):
        values = sample
    else:
        try:
            values = json.loads(sample)
            if not isinstance(values, list) and not isinstance(values,dict):
                values = [values]
        except:
            try:
                values = eval(sample)
                if isinstance(values, tuple):
                    values = list(values)
            except:
                try:
                    values = [float(sample)]
                except:
                    try:
                        values = list(map(float, values.split(',')))
                    except:
                        values = [sample]
    return values

def convert_sample_short(sample):
    try:
        values = json.loads(sample)
    except:
        try:
            values = list(map(float, sample.replace("[","").replace("]","").replace("(","").replace(")","").split(',')))
        except:
            try:
                values = [float(sample)]
            except:
                values = [sample]
    return values

#convert_sample('(0.0024687682368556008, 0.17776913487103307, 0.2295764062106903, 0.09898929381168664, 0.5109892310134816)')