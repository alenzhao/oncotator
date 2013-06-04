"""
# By downloading the PROGRAM you agree to the following terms of use:
#
# BROAD INSTITUTE SOFTWARE LICENSE AGREEMENT
# FOR ACADEMIC NON-COMMERCIAL RESEARCH PURPOSES ONLY
#
# This Agreement is made between the Broad Institute, Inc. with a principal address at 7 Cambridge Center, Cambridge, MA 02142 ("BROAD") and the LICENSEE and is effective at the date the downloading is completed ("EFFECTIVE DATE").
# WHEREAS, LICENSEE desires to license the PROGRAM, as defined hereinafter, and BROAD wishes to have this PROGRAM utilized in the public interest, subject only to the royalty-free, nonexclusive, nontransferable license rights of the United States Government pursuant to 48 CFR 52.227-14; and
# WHEREAS, LICENSEE desires to license the PROGRAM and BROAD desires to grant a license on the following terms and conditions.
# NOW, THEREFORE, in consideration of the promises and covenants made herein, the parties hereto agree as follows:
#
# 1. DEFINITIONS
# 1.1	"PROGRAM" shall mean copyright in the object code and source code known as Oncotator and related documentation, if any, as they exist on the EFFECTIVE DATE and can be downloaded from http://www.broadinstitute.org/cancer/cga/oncotator on the EFFECTIVE DATE.
#
# 2. LICENSE
# 2.1   Grant. Subject to the terms of this Agreement, BROAD hereby grants to LICENSEE, solely for academic non-commercial research purposes, a non-exclusive, non-transferable license to: (a) download, execute and display the PROGRAM and (b) create bug fixes and modify the PROGRAM.
# LICENSEE hereby automatically grants to BROAD a non-exclusive, royalty-free, irrevocable license to any LICENSEE bug fixes or modifications to the PROGRAM with unlimited rights to sublicense and/or distribute.  LICENSEE agrees to provide any such modifications and bug fixes to BROAD promptly upon their creation.
# The LICENSEE may apply the PROGRAM in a pipeline to data owned by users other than the LICENSEE and provide these users the results of the PROGRAM provided LICENSEE does so for academic non-commercial purposes only.  For clarification purposes, academic sponsored research is not a commercial use under the terms of this Agreement.
# 2.2  No Sublicensing or Additional Rights. LICENSEE shall not sublicense or distribute the PROGRAM, in whole or in part, without prior written permission from BROAD.  LICENSEE shall ensure that all of its users agree to the terms of this Agreement.  LICENSEE further agrees that it shall not put the PROGRAM on a network, server, or other similar technology that may be accessed by anyone other than the LICENSEE and its employees and users who have agreed to the terms of this agreement.
# 2.3  License Limitations. Nothing in this Agreement shall be construed to confer any rights upon LICENSEE by implication, estoppel, or otherwise to any computer software, trademark, intellectual property, or patent rights of BROAD, or of any other entity, except as expressly granted herein. LICENSEE agrees that the PROGRAM, in whole or part, shall not be used for any commercial purpose, including without limitation, as the basis of a commercial software or hardware product or to provide services. LICENSEE further agrees that the PROGRAM shall not be copied or otherwise adapted in order to circumvent the need for obtaining a license for use of the PROGRAM.
#
# 3. OWNERSHIP OF INTELLECTUAL PROPERTY
# LICENSEE acknowledges that title to the PROGRAM shall remain with BROAD. The PROGRAM is marked with the following BROAD copyright notice and notice of attribution to contributors. LICENSEE shall retain such notice on all copies.  LICENSEE agrees to include appropriate attribution if any results obtained from use of the PROGRAM are included in any publication.
#
# Copyright 2012 Broad Institute, Inc.
# Notice of attribution:  The Oncotator program was made available through the generosity of the Cancer Genome Analysis group at the Broad Institute, Inc.
#
# LICENSEE shall not use any trademark or trade name of BROAD, or any variation, adaptation, or abbreviation, of such marks or trade names, or any names of officers, faculty, students, employees, or agents of BROAD except as states above for attribution purposes.
#
# 4. INDEMNIFICATION
# LICENSEE shall indemnify, defend, and hold harmless BROAD, and their respective officers, faculty, students, employees, associated investigators and agents, and their respective successors, heirs and assigns, ("Indemnitees"), against any liability, damage, loss, or expense (including reasonable attorneys fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, actions, demands or judgments arising out of any theory of liability (including, without limitation, actions in the form of tort, warranty, or strict liability and regardless of whether such action has any factual basis) pursuant to any right or license granted under this Agreement.
#
# 5. NO REPRESENTATIONS OR WARRANTIES
# THE PROGRAM IS DELIVERED "AS IS."  BROAD MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE PROGRAM OR THE COPYRIGHT, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, WHETHER OR NOT DISCOVERABLE. BROAD EXTENDS NO WARRANTIES OF ANY KIND AS TO PROGRAM CONFORMITY WITH WHATEVER USER MANUALS OR OTHER LITERATURE MAY BE ISSUED FROM TIME TO TIME.
# IN NO EVENT SHALL BROAD OR ITS RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATED INVESTIGATORS AND AFFILIATES BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES OF ANY KIND, INCLUDING, WITHOUT LIMITATION, ECONOMIC DAMAGES OR INJURY TO PROPERTY AND LOST PROFITS, REGARDLESS OF WHETHER BROAD SHALL BE ADVISED, SHALL HAVE OTHER REASON TO KNOW, OR IN FACT SHALL KNOW OF THE POSSIBILITY OF THE FOREGOING.
#
# 6. ASSIGNMENT
# This Agreement is personal to LICENSEE and any rights or obligations assigned by LICENSEE without the prior written consent of BROAD shall be null and void.
#
# 7. MISCELLANEOUS
# 7.1 Export Control. LICENSEE gives assurance that it will comply with all United States export control laws and regulations controlling the export of the PROGRAM, including, without limitation, all Export Administration Regulations of the United States Department of Commerce. Among other things, these laws and regulations prohibit, or require a license for, the export of certain types of software to specified countries.
# 7.2 Termination. LICENSEE shall have the right to terminate this Agreement for any reason upon prior written notice to BROAD. If LICENSEE breaches any provision hereunder, and fails to cure such breach within thirty (30) days, BROAD may terminate this Agreement immediately. Upon termination, LICENSEE shall provide BROAD with written assurance that the original and all copies of the PROGRAM have been destroyed, except that, upon prior written authorization from BROAD, LICENSEE may retain a copy for archive purposes.
# 7.3 Survival. The following provisions shall survive the expiration or termination of this Agreement: Articles 1, 3, 4, 5 and Sections 2.2, 2.3, 7.3, and 7.4.
# 7.4 Notice. Any notices under this Agreement shall be in writing, shall specifically refer to this Agreement, and shall be sent by hand, recognized national overnight courier, confirmed facsimile transmission, confirmed electronic mail, or registered or certified mail, postage prepaid, return receipt requested.  All notices under this Agreement shall be deemed effective upon receipt.
# 7.5 Amendment and Waiver; Entire Agreement. This Agreement may be amended, supplemented, or otherwise modified only by means of a written instrument signed by all parties. Any waiver of any rights or failure to act in a specific instance shall relate only to such instance and shall not be construed as an agreement to waive any rights or fail to act in any other instance, whether or not similar. This Agreement constitutes the entire agreement among the parties with respect to its subject matter and supersedes prior agreements or understandings between the parties relating to its subject matter.
# 7.6 Binding Effect; Headings. This Agreement shall be binding upon and inure to the benefit of the parties and their respective permitted successors and assigns. All headings are for convenience only and shall not affect the meaning of any provision of this Agreement.
# 7.7 Governing Law. This Agreement shall be construed, governed, interpreted and applied in accordance with the internal laws of the Commonwealth of Massachusetts, U.S.A., without regard to conflict of laws principles.
#"""


'''
Created on Nov 7, 2012

@author: lichtens
'''
from OutputRenderer import OutputRenderer
from oncotator.utils.ConfigUtils import ConfigUtils
import copy
import csv
import collections
import logging
import os
import sys
import tempfile
import itertools
import operator
import string
import vcf
import heapq

from oncotator.input.ConfigInputIncompleteException import ConfigInputIncompleteException
from oncotator.utils.TsvFileSorter import TsvFileSorter


class _OutputAnnotation:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.dataType = "String"
        self.description = "Unknown"
        self.columnName = "FORMAT"
        self.number = "."

    def __str__(self):
        s = ''
        if self.columnName == "INFO":
            s = "INFO=<ID=" + self.id + ",Number=" + str(self.number) + ",Type=" + self.dataType + ",Description=\"" + self.description + "\">"
        elif self.columnName == "FORMAT":
            s = "FORMAT=<ID=" + self.id + ",Number=" + str(self.number) + ",Type=" + self.dataType + ",Description=\"" + self.description + "\">"
        elif self.columnName == "FILTER":
            s = "FILTER=<ID=" + self.name + ",Description=\"" + self.description + "\">"
        return s

    def setColumnName(self, colName):
        self.columnName = colName
   
    def setDataType(self, dt):
        self.dataType = dt
    
    def setDescription(self, desc):
        self.description = desc

    def setID(self, ID):
        self.id = ID
    
    def setNumber(self, num):
        self.number = num

    def getColumnName(self):
        return self.columnName
    
    def getDataType(self):
        return self.dataType

    def getDescription(self):
        return self.description

    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getNumber(self):
        return self.number

class VcfOutputRenderer(OutputRenderer):
    '''
    The SimpleOutputRenderer renders a basic tsv file from the given mutations.  All annotations are included with real names as column headers.
    
    Header is determined by the first mutation given.
    
    No attention is paid to order of the headers.    
    '''
    _Annotation = collections.namedtuple(typename="Annotation", field_names=["ID","description","type","num"]) # use annotationName as key
    _tsvTuple = collections.namedtuple(typename="tsvTuple", field_names=["chrom","pos","sampleName","line"])
    _Pair = collections.namedtuple(typename="Pair", field_names=["key","value"])

    def __getRecordTuple(self,line,delimiter=','):
        tokens = line.split(delimiter)
        chrom = int(tokens[0]) 
        pos = int(tokens[1])
        sampleName = tokens[2]
        return self.Record(chrom=chrom,pos=pos,sampleName=sampleName,line=line)

    def __init__(self,filename, datasources=[], configFile='vcf.out.config'):
        '''
        Constructor
        '''
        self._filename = filename
        self.logger = logging.getLogger(__name__)
        self._datasources = datasources
        self.config = ConfigUtils.createConfigParser(configFile,ignoreCase=False)
        self.annotationTable = dict()
        self.chromHashCodeTable = None
        self.configTable = dict()
        self.delimiter = '\t'
        self.reservedAnnotationNames = ['chr', 'start', 'sampleName', 'ref_allele', 'alt_allele', 'end', 'build', 'altAlleleSeen']
        
    def __setOutputAnnotationID(self, annotation):
        ID = None
        name = annotation.getName()
        if name in self.configTable["INFO"]:
            ID = self.configTable["INFO"][name]
        elif name in self.configTable["FORMAT"]:
            ID = self.configTable["FORMAT"][name]
        elif name in self.configTable["OTHER"]:
            ID = self.configTable["OTHER"][name]
        if ID is None:
            ID = name
        annotation.setID(ID=ID)
        return annotation
        
    def __setOutputAnnotationColumnName(self, annotation, mutation):
        columnName = ''
        name = annotation.getName()
        if not columnName: # (a) tags 
            tags = mutation.getAnnotation(name).getTags()
            if isinstance(tags,list) and len(tags) > 0:
                columnName = tags.pop(0)
            if columnName and columnName == "aggregate":
                columnName = "INFO"
            elif columnName and columnName == "variant":
                columnName = "FORMAT"
            elif columnName and columnName == "filter":
                columnName = "FILTER"
    
        if not columnName: # (b) config
            if name in self.configTable["INFO"]:
                columnName = "INFO"
            elif name in self.configTable["FORMAT"]:
                name = "FORMAT"
            elif name in self.configTable["OTHER"]:
                columnName = self.configTable["OTHER"][name]

        if not columnName: # (c) PyVCF defaults
            if name.upper() in vcf.parser.RESERVED_INFO:
                columnName = "INFO"
            elif name.upper() in vcf.parser.RESERVED_FORMAT:
                columnName = "FORMAT"

        if not columnName: # (d) default: FORMAT
            columnName = "FORMAT"
        annotation.setColumnName(colName=columnName)
        return annotation

    def __setOutputAnnotationDescription(self, annotation, mutation):
        name = annotation.getName()
        columnName = annotation.getColumnName()
        description = mutation.getAnnotation(name).getDescription()
               
        # description in the config files overwrite the description in the mutation
        if (columnName == "FILTER") and ("FILTER_DESCRIPTION" in self.configTable) and (columnName in self.configTable["FILTER_DESCRIPTION"]):
            description = self.configTable["FILTER_DESCRIPTION"][columnName]
        elif (columnName == "FORMAT") and ("FORMAT_DESCRIPTION" in self.configTable) and (columnName in self.configTable["FORMAT_DESCRIPTION"]):
            description = self.configTable["FORMAT_DESCRIPTION"][columnName]
        elif (columnName == "INFO") and ("INFO_DESCRIPTION" in self.configTable) and (columnName in self.configTable["INFO_DESCRIPTION"]):
            description = self.configTable["INFO_DESCRIPTION"][columnName]
            
        if not description: 
            description = "Unknown"
        annotation.setDescription(desc=description)
        return annotation

    def __setOutputAnnotationDataType(self, annotation, mutation):
        name = annotation.getName()
        columnName = annotation.getColumnName()
        ID = annotation.getID()
        dataType = mutation.getAnnotation(name).getDataType()
        
        if not dataType or dataType == ".": # data type was not specified
            if columnName == "FILTER":
                if ID in vcf.parser.RESERVED_INFO:
                    dataType = vcf.parser.RESERVED_INFO[ID]
            elif columnName == "FORMAT":
                if ID in vcf.parser.RESERVED_FORMAT:
                    dataType = vcf.parser.RESERVED_FORMAT[ID]
        annotation.setDataType(dt=dataType)
        return annotation
    
    def __setOutputAnnotationNumber(self, annotation, mutation):
        name = annotation.getName()
        number = mutation.getAnnotation(name).getNumber()
        annotation.setNumber(num=number)
        return annotation
    
    def __createOutputAnnotationTable(self, mutation, annotationNames):
        for annotationName in annotationNames: # iterate over annotations
            if annotationName not in self.reservedAnnotationNames:
                annotation = _OutputAnnotation(name=annotationName)
                annotation = self.__setOutputAnnotationID(annotation=annotation)
                annotation = self.__setOutputAnnotationColumnName(annotation=annotation, mutation=mutation)
                annotation = self.__setOutputAnnotationDescription(annotation=annotation, mutation=mutation)
                annotation = self.__setOutputAnnotationDataType(annotation=annotation, mutation=mutation)
                annotation = self.__setOutputAnnotationNumber(annotation=annotation, mutation=mutation)
            
                columnName = annotation.getColumnName()
                if columnName not in self.annotationTable:
                    self.annotationTable[columnName] = dict()
                self.annotationTable[columnName][annotationName] = annotation
        
        # sort each dictionary by ID
        for columnName in self.annotationTable:
            self.annotationTable[columnName] = collections.OrderedDict(sorted(self.annotationTable[columnName].iteritems(), key=lambda annotation: annotation[1].getID()))
    
    def __getAnnotationNames(self, mutation):
        # Parse header for the intermediate tsv file
        annotationNames = copy.copy(self.reservedAnnotationNames) # fixed annotationNames (shallow copy)
        for annotationName in mutation.keys():
            if annotationName not in annotationNames:
                annotationNames.append(annotationName)
        return annotationNames
    
    def renderMutations(self, mutations, comments=[]):
        ''' Generate a simple tsv file based on the incoming mutations.
        
        Assumes that all mutations have the same annotations, even if some are not populated.
        
        Returns a file name. '''
        
        # Parse the config file
        for sectionKey in ["INFO","FORMAT","OTHER"]: # required sections for annotations
            if ConfigUtils.hasSectionKey(configParser=self.config, sectionKey=sectionKey):
                self.configTable[sectionKey] = ConfigUtils.buildReverseAlternativeDictionaryFromConfig(configParser=self.config, sectionKey=sectionKey)
            else:
                raise ConfigInputIncompleteException("Missing %s section in the output config file." % sectionKey)

        for sectionKey in ["INFO_DESCRIPTION","FILTER_DESCRIPTION","FORMAT_DESCRIPTION"]: # optional sections for specifying description
            if ConfigUtils.hasSectionKey(configParser=self.config, sectionKey=sectionKey):
                self.configTable[sectionKey] = ConfigUtils.buildAlternateKeyDictionaryFromConfig(configParser=self.config, sectionKey=sectionKey)
                for ID in self.configTable[sectionKey]:
                    self.configTable[sectionKey][ID] = string.join(words=self.configTable[sectionKey][ID], sep=",")
       
        path = os.getcwd()
        temp = tempfile.NamedTemporaryFile(dir=path) # create a temporary file to write tab-separated file
        
        self.logger.info("Rendering VCF output file: " + self._filename)
        self.logger.info("Data sources included: " + str(self._datasources))
        self.logger.info("Render starting...")
        
        flg = False
        for comment in comments: 
            if comment.startswith('fileformat=VCFv4.'):
                comments[0] = '##' + comments[0]
                flg = True
                break
        if not flg:
            comments.insert(0,'##fileformat=VCFv4.1')
        
        ctr = 0
        headers = comments[0:len(comments)-1] if (comments is not None) and (len(comments) > 0) else list()
        header = None
        sampleNames = set()
        annotationNames = None
        chroms = set()
                
        fp = open(temp.name,'w') # output to a tab-delimited file 
        dw = None
        # Write mutation data to a temporary tab-delimited file
        for m in mutations:           
            if header is None: # first mutation contains all the required information
                annotationNames = self.__getAnnotationNames(mutation=m)
                self.__createOutputAnnotationTable(mutation=m, annotationNames=annotationNames)
                columnNames = ["INFO","FORMAT","FILTER"]
                for columnName in columnNames:
                    annotations = self.annotationTable[columnName]
                    for annotation in annotations:
                        headers.append(str(self.annotationTable[columnName][annotation]))
                header = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']

            # Sample names (set)
            sampleName = m.getAnnotation('sampleName').getValue()
            if sampleName not in sampleNames:
                sampleNames.add(sampleName)

            # Parse chromosome
            chrom = m.getAnnotation('chr').getValue()
            if chrom not in chroms:
                chroms.add(chrom)
            
            if dw is None: # initialize the CSV dictionary writer
                dw = csv.DictWriter(fp,annotationNames,delimiter=self.delimiter,lineterminator="\n")
                dw.writeheader()
                
            dw.writerow(m)
            ctr = ctr + 1
        fp.close() # writing to intermediate TSV file was complete
        
        # Sort the temporary tab-delimited file first by sampleName, then by start, and lastly by chr
        if self.chromHashCodeTable is None:
            self.chromHashCodeTable = self.__createChromHashCodeTable(chroms=chroms)
        temp = self.__sort(readfilename=temp.name, path=path)  

        if len(sampleNames) > 0:
            sampleNames = list(sampleNames) # convert to list to preserve ordering
            sampleNames.sort() # lexicographic ordering of sampleNames
            header = header.append(sampleNames)
        
        # Build VCF record each variant at a time
        sampleNameIndexes = None
        if len(sampleNames) > 0:
            sampleNameIndexes = dict([(sampleName,index) for (index,sampleName) in enumerate(sampleNames)])
        with open(temp.name,'r') as fp:
            chrom = None
            pos = None
            varData = list()
            dr = csv.DictReader(fp,delimiter=self.delimiter)
            for data in dr:
                if (chrom != data['chr']) or ((chrom == data['chr']) and (pos != data['start'])): # new position either on a different chromosome or on the same chromosome
                    chrom = data['chr']
                    pos = data['start']
                    #if len(varData) > 0:
                        # create record
                        #record = self.__createRecord(varData=varData)
                    varData = list()
                    varData.append(data)
                else: 
                    varData.append(data)
        
        if len(varData) > 0:
            varData
        
        fp = file(self._filename,'w')
        fp.write(string.join(headers,'\n##'))
        fp.close()
        return self._filename
            
        '''
                
        f = open(temp.name,'r')
        for line in f.readlines():
            print line.rstrip('\n')
        
        print "Rendered " + str(ctr) + " mutations"'''
    
       


    def __sort(self, readfilename, path):
        writefile = tempfile.NamedTemporaryFile(dir=path)
        TsvFileSorter.sortFile(readfilename, writefile.name)
        return writefile

    def __createChromHashCodeTable(self, chroms):
        chromHashCodeTable = dict()
        highestHashCode = 0
        for chrom in chroms:
            chromHashCodeTable[chrom] = None
            if chrom.isdigit():
                chromHashCodeTable[chrom] = int(chrom)
                if highestHashCode < chromHashCodeTable[chrom]:
                    highestHashCode = chromHashCodeTable[chrom]
        index = 0
        for chrom in sorted(chroms):
            if chromHashCodeTable[chrom] is None:
                if chrom.upper() == 'X': # X chromosome
                    chromHashCodeTable[chrom] = highestHashCode + 1
                elif chrom.upper() == 'Y': # Y chrmomosome
                    chromHashCodeTable[chrom] = highestHashCode + 2
                elif (chrom.upper() == 'M') or (chrom.upper() == 'MT'): # mitochondrial chrmomosome
                    chromHashCodeTable[chrom] = highestHashCode + 3
                else:
                    index += 1
                    chromHashCodeTable[chrom] = highestHashCode + index + 3
        return chromHashCodeTable
        