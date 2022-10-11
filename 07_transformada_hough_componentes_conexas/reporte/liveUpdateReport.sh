#!/bin/bash

do-after-change "pandoc -i reporte/reporte.md -o reporte/reporte.pdf" reporte/reporte.md

