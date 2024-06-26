# Copyright 2024 Thales DIS France SAS
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
#
# Original Author: Oukalrazqou Abdessamii
""" Module is used to factorize multiples registers with the same name to 
    a specific format of registers """

import argparse
from libs.utils import CsrParser
from libs.utils import IsaParser
from libs.utils import IsaGenerator
from libs.utils import CsrGenerator
from libs.utils import RstAddressBlock
from libs.utils import MdAddressBlock
from libs.utils import InstrstBlock
from libs.utils import InstmdBlock

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ipxact2rst")
    parser.add_argument("-s", "--srcFile", help="yaml input file")
    parser.add_argument("-d", "--destDir", help="write generated file to dir")
    parser.add_argument("-m", "--modif", help="ISA Formatter if existe")
    parser.add_argument("-i", "--temp", help="Full ISA Template")
    parser.add_argument("-t", "--target", help="Specifiy Config Name")
    args, unknown_args = parser.parse_known_args()
    if args.temp:
        e = IsaParser(args.srcFile, args.temp, args.target, args.modif)
        document = e.returnDocument()
        generator = IsaGenerator(args.target)
        generator.generateISA(InstrstBlock, document)
        generator.generateISA(InstmdBlock, document)
    else:
        e = CsrParser(args.srcFile, args.target, args.modif)
        document = e.returnDocument()
        generator = CsrGenerator(args.target)
        generator.generateCSR(RstAddressBlock, document)
        generator.generateCSR(MdAddressBlock, document)
