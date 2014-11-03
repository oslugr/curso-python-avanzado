#!/bin/bash

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

############################################################################
# Requirements:
#	* You need 'xclip' shell app installed before use this script.
#
# To use this script:
# * Give exec permissions to this script and run it as "./html2clipboard"
# * Or run it as "bash html2clipboard" if you didn't give exec. permissions
#
# For each file html in the folder, the content is copied to clipboard and
# wait to a key press for continue.
############################################################################

for file in $(ls *.html)
do
    echo ${file}
    cat $file | xclip -selection clipboard
    echo "$file copied to clipboard"
    read
done