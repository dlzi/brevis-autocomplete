import sublime_plugin
import sublime

brevis_classes = ["bxs--brdrbx","bxs--ctbx","bxs--brdrbx-s","bxs--ctbx-s","bxs--brdrbx-m","bxs--ctbx-m","bxs--brdrbx-l","bxs--ctbx-l","d--blk","d--fx","d--in","d--inblk","d--intbl","d--infx","d--n","d--tbl","d--tblcl","d--tblrw","d--tblrwgrp","d--tblcol","d--tblcolgrp","d--blk-s","d--fx-s","d--in-s","d--inblk-s","d--intbl-s","d--infx-s","d--n-s","d--tbl-s","d--tblcl-s","d--tblrw-s","d--tblrwgrp-s","d--tblcol-s","d--tblcolgrp-s","d--blk-m","d--fx-m","d--in-m","d--inblk-m","d--intbl-m","d--infx-m","d--n-m","d--tbl-m","d--tblcl-m","d--tblrw-m","d--tblrwgrp-m","d--tblcol-m","d--tblcolgrp-m","d--blk-l","d--fx-l","d--in-l","d--inblk-l","d--intbl-l","d--infx-l","d--n-l","d--tbl-l","d--tblcl-l","d--tblrw-l","d--tblrwgrp-l","d--tblcol-l","d--tblcolgrp-l","pos--sta","pos--rel","pos--abs","pos--fix","pos--sta-s","pos--rel-s","pos--abs-s","pos--fix-s","pos--sta-n","pos--rel-n","pos--abs-n","pos--fix-n","pos--sta-l","pos--rel-l","pos--abs-l","pos--fix-l","t--0","t--1","t--2","t--3","t--4","t--5","t--6","t--7","t--8","t--n1","t--n2","t--n3","t--n4","t--n5","t--n6","t--n7","t--n8","t--0-s","t--1-s","t--2-s","t--3-s","t--4-s","t--5-s","t--6-s","t--7-s","t--8-s","t--n1-s","t--n2-s","t--n3-s","t--n4-s","t--n5-s","t--n6-s","t--n7-s","t--n8-s","t--0-m","t--1-m","t--2-m","t--3-m","t--4-m","t--5-m","t--6-m","t--7-m","t--8-m","t--n1-m","t--n2-m","t--n3-m","t--n4-m","t--n5-m","t--n6-m","t--n7-m","t--n8-m","t--0-l","t--1-l","t--2-l","t--3-l","t--4-l","t--5-l","t--6-l","t--7-l","t--8-l","t--n1-l","t--n2-l","t--n3-l","t--n4-l","t--n5-l","t--n6-l","t--n7-l","t--n8-l","r--0","r--1","r--2","r--3","r--4","r--5","r--6","r--7","r--8","r--n1","r--n2","r--n3","r--n4","r--n5","r--n6","r--n7","r--n8","r--0-s","r--1-s","r--2-s","r--3-s","r--4-s","r--5-s","r--6-s","r--7-s","r--8-s","r--n1-s","r--n2-s","r--n3-s","r--n4-s","r--n5-s","r--n6-s","r--n7-s","r--n8-s","r--0-m","r--1-m","r--2-m","r--3-m","r--4-m","r--5-m","r--6-m","r--7-m","r--8-m","r--n1-m","r--n2-m","r--n3-m","r--n4-m","r--n5-m","r--n6-m","r--n7-m","r--n8-m","r--0-l","r--1-l","r--2-l","r--3-l","r--4-l","r--5-l","r--6-l","r--7-l","r--8-l","r--n1-l","r--n2-l","r--n3-l","r--n4-l","r--n5-l","r--n6-l","r--n7-l","r--n8-l","b--0","b--1","b--2","b--3","b--4","b--5","b--6","b--7","b--8","b--n1","b--n2","b--n3","b--n4","b--n5","b--n6","b--n7","b--n8","b--0-s","b--1-s","b--2-s","b--3-s","b--4-s","b--5-s","b--6-s","b--7-s","b--8-s","b--n1-s","b--n2-s","b--n3-s","b--n4-s","b--n5-s","b--n6-s","b--n7-s","b--n8-s","b--0-m","b--1-m","b--2-m","b--3-m","b--4-m","b--5-m","b--6-m","b--7-m","b--8-m","b--n1-m","b--n2-m","b--n3-m","b--n4-m","b--n5-m","b--n6-m","b--n7-m","b--n8-m","b--0-l","b--1-l","b--2-l","b--3-l","b--4-l","b--5-l","b--6-l","b--7-l","b--8-l","b--n1-l","b--n2-l","b--n3-l","b--n4-l","b--n5-l","b--n6-l","b--n7-l","b--n8-l","l--0","l--1","l--2","l--3","l--4","l--5","l--6","l--7","l--8","l--n1","l--n2","l--n3","l--n4","l--n5","l--n6","l--n7","l--n8","l--0-s","l--1-s","l--2-s","l--3-s","l--4-s","l--5-s","l--6-s","l--7-s","l--8-s","l--n1-s","l--n2-s","l--n3-s","l--n4-s","l--n5-s","l--n6-s","l--n7-s","l--n8-s","l--0-m","l--1-m","l--2-m","l--3-m","l--4-m","l--5-m","l--6-m","l--7-m","l--8-m","l--n1-m","l--n2-m","l--n3-m","l--n4-m","l--n5-m","l--n6-m","l--n7-m","l--n8-m","l--0-l","l--1-l","l--2-l","l--3-l","l--4-l","l--5-l","l--6-l","l--7-l","l--8-l","l--n1-l","l--n2-l","l--n3-l","l--n4-l","l--n5-l","l--n6-l","l--n7-l","l--n8-l","f--r","f--l","f--n","f--r-s","f--l-s","f--n-s","f--r-m","f--l-m","f--n-m","f--r-l","f--l-l","f--n-l","clr--r","clr--l","clr--bh","clr--n","clr--r-s","clr--l-s","clr--bh-s","clr--n-s","clr--r-m","clr--l-m","clr--bh-m","clr--n-m","clr--r-l","clr--l-l","clr--bh-l","clr--n-l","fx--a","fx--ini","fx--n","fx--a-s","fx--ini-s","fx--n-s","fx--a-m","fx--ini-m","fx--n-m","fx--a-l","fx--ini-l","fx--n-l","fxbs--0","fxbs--1","fxbs--2","fxbs--3","fxbs--4","fxbs--5","fxbs--6","fxbs--7","fxbs--8","fxbs--a","fxbs--0-s","fxbs--1-s","fxbs--2-s","fxbs--3-s","fxbs--4-s","fxbs--5-s","fxbs--6-s","fxbs--7-s","fxbs--8-s","fxbs--a-s","fxbs--0-m","fxbs--1-m","fxbs--2-m","fxbs--3-m","fxbs--4-m","fxbs--5-m","fxbs--6-m","fxbs--7-m","fxbs--8-m","fxbs--a-m","fxbs--0-l","fxbs--1-l","fxbs--2-l","fxbs--3-l","fxbs--4-l","fxbs--5-l","fxbs--6-l","fxbs--7-l","fxbs--8-l","fxbs--a-l","fxdir--col","fxdir--colrvs","fxdir--rw","fxdir--rwrvs","fxdir--col-s","fxdir--colrvs-s","fxdir--rw-s","fxdir--rwrvs-s","fxdir--col-m","fxdir--colrvs-m","fxdir--rw-m","fxdir--rwrvs-m","fxdir--col-l","fxdir--colrvs-l","fxdir--rw-l","fxdir--rwrvs-l","fxfw--rwwp","fxfw--rwrvsn","fxfw--colwprvs","fxfw--colwp","fxfw--rwwp-s","fxfw--rwrvsn-s","fxfw--colwprvs-s","fxfw--colwp-s","fxfw--rwwp-m","fxfw--rwrvsn-m","fxfw--colwprvs-m","fxfw--colwp-m","fxfw--rwwp-l","fxfw--rwrvsn-l","fxfw--colwprvs-l","fxfw--colwp-l","fxgw--0","fxgw--1","fxgw--0-s","fxgw--1-s","fxgw--0-m","fxgw--1-m","fxgw--0-l","fxgw--1-l","fxsk--0","fxsk--1","fxsk--0-s","fxsk--1-s","fxsk--0-m","fxsk--1-m","fxsk--0-l","fxsk--1-l","fxwp--n","fxwp--wp","fxwp--wprvs","fxwp--n-s","fxwp--wp-s","fxwp--wprvs-s","fxwp--n-m","fxwp--wp-m","fxwp--wprvs-m","fxwp--n-l","fxwp--wp-l","fxwp--wprvs-l","anct--ctr","anct--fxe","anct--fxst","anct--spard","anct--spbtw","anct--ctr-s","anct--fxe-s","anct--fxst-s","anct--spard-s","anct--spbtw-s","anct--ctr-m","anct--fxe-m","anct--fxst-m","anct--spard-m","anct--spbtw-m","anct--ctr-l","anct--fxe-l","anct--fxst-l","anct--spard-l","anct--spbtw-l","anis--ble","anis--ctr","anis--fxe","anis--fxst","anis--str","anis--ble-s","anis--ctr-s","anis--fxe-s","anis--fxst-s","anis--str-s","anis--ble-m","anis--ctr-m","anis--fxe-m","anis--fxst-m","anis--str-m","anis--ble-l","anis--ctr-l","anis--fxe-l","anis--fxst-l","anis--str-l","ansf--a","ansf--ctr","ansf--fxe","ansf--fxst","ansf--str","ansf--a-s","ansf--ctr-s","ansf--fxe-s","ansf--fxst-s","ansf--str-s","ansf--a-m","ansf--ctr-m","ansf--fxe-m","ansf--fxst-m","ansf--str-m","ansf--a-l","ansf--ctr-l","ansf--fxe-l","ansf--fxst-l","ansf--str-l","jct--ctr","jct--fxe","jct--fxst","jct--spard","jct--spbtw","jct--ctr-s","jct--fxe-s","jct--fxst-s","jct--spard-s","jct--spbtw-s","jct--ctr-m","jct--fxe-m","jct--fxst-m","jct--spard-m","jct--spbtw-m","jct--ctr-l","jct--fxe-l","jct--fxst-l","jct--spard-l","jct--spbtw-l","jis--ctr","jis--fxe","jis--fxst","jis--sfst","jis--sfe","jis--ctr-s","jis--fxe-s","jis--fxst-s","jis--sfst-s","jis--sfe-s","jis--ctr-m","jis--fxe-m","jis--fxst-m","jis--sfst-m","jis--sfe-m","jis--ctr-l","jis--fxe-l","jis--fxst-l","jis--sfst-l","jis--sfe-l","jsf--ctr","jsf--fxe","jsf--fxst","jsf--sfst","jsf--sfe","jsf--ctr-s","jsf--fxe-s","jsf--fxst-s","jsf--sfst-s","jsf--sfe-s","jsf--ctr-m","jsf--fxe-m","jsf--fxst-m","jsf--sfst-m","jsf--sfe-m","jsf--ctr-l","jsf--fxe-l","jsf--fxst-l","jsf--sfst-l","jsf--sfe-l","v--hid","v--v","v--hid-s","v--v-s","v--hid-m","v--v-m","v--hid-l","v--v-l","o--0","o--25","o--50","o--75","o--100","o--0-s","o--25-s","o--50-s","o--75-s","o--100-s","o--0-m","o--25-m","o--50-m","o--75-m","o--100-m","o--0-l","o--25-l","o--50-l","o--75-l","o--100-l","zidx--a","zidx--1","zidx--2","zidx--3","zidx--4","zidx--5","zidx--6","zidx--7","zidx--8","zidx--a-s","zidx--1-s","zidx--2-s","zidx--3-s","zidx--4-s","zidx--5-s","zidx--6-s","zidx--7-s","zidx--8-s","zidx--a-m","zidx--1-m","zidx--2-m","zidx--3-m","zidx--4-m","zidx--5-m","zidx--6-m","zidx--7-m","zidx--8-m","zidx--a-l","zidx--1-l","zidx--2-l","zidx--3-l","zidx--4-l","zidx--5-l","zidx--6-l","zidx--7-l","zidx--8-l","m--0","m--1","m--2","m--3","m--4","m--5","m--6","m--7","m--8","m--n1","m--n2","m--n3","m--n4","m--n5","m--n6","m--n7","m--n8","m--0-s","m--1-s","m--2-s","m--3-s","m--4-s","m--5-s","m--6-s","m--7-s","m--8-s","m--n1-s","m--n2-s","m--n3-s","m--n4-s","m--n5-s","m--n6-s","m--n7-s","m--n8-s","m--0-m","m--1-m","m--2-m","m--3-m","m--4-m","m--5-m","m--6-m","m--7-m","m--8-m","m--n1-m","m--n2-m","m--n3-m","m--n4-m","m--n5-m","m--n6-m","m--n7-m","m--n8-m","m--0-l","m--1-l","m--2-l","m--3-l","m--4-l","m--5-l","m--6-l","m--7-l","m--8-l","m--n1-l","m--n2-l","m--n3-l","m--n4-l","m--n5-l","m--n6-l","m--n7-l","m--n8-l","mt--0","mt--1","mt--2","mt--3","mt--4","mt--5","mt--6","mt--7","mt--8","mt--n1","mt--n2","mt--n3","mt--n4","mt--n5","mt--n6","mt--n7","mt--n8","mt--0-s","mt--1-s","mt--2-s","mt--3-s","mt--4-s","mt--5-s","mt--6-s","mt--7-s","mt--8-s","mt--n1-s","mt--n2-s","mt--n3-s","mt--n4-s","mt--n5-s","mt--n6-s","mt--n7-s","mt--n8-s","mt--0-m","mt--1-m","mt--2-m","mt--3-m","mt--4-m","mt--5-m","mt--6-m","mt--7-m","mt--8-m","mt--n1-m","mt--n2-m","mt--n3-m","mt--n4-m","mt--n5-m","mt--n6-m","mt--n7-m","mt--n8-m","mt--0-l","mt--1-l","mt--2-l","mt--3-l","mt--4-l","mt--5-l","mt--6-l","mt--7-l","mt--8-l","mt--n1-l","mt--n2-l","mt--n3-l","mt--n4-l","mt--n5-l","mt--n6-l","mt--n7-l","mt--n8-l","mr--a","mr--0","mr--1","mr--2","mr--3","mr--4","mr--5","mr--6","mr--7","mr--8","mr--n1","mr--n2","mr--n3","mr--n4","mr--n5","mr--n6","mr--n7","mr--n8","mr--a-s","mr--0-s","mr--1-s","mr--2-s","mr--3-s","mr--4-s","mr--5-s","mr--6-s","mr--7-s","mr--8-s","mr--n1-s","mr--n2-s","mr--n3-s","mr--n4-s","mr--n5-s","mr--n6-s","mr--n7-s","mr--n8-s","mr--a-m","mr--0-m","mr--1-m","mr--2-m","mr--3-m","mr--4-m","mr--5-m","mr--6-m","mr--7-m","mr--8-m","mr--n1-m","mr--n2-m","mr--n3-m","mr--n4-m","mr--n5-m","mr--n6-m","mr--n7-m","mr--n8-m","mr--a-l","mr--0-l","mr--1-l","mr--2-l","mr--3-l","mr--4-l","mr--5-l","mr--6-l","mr--7-l","mr--8-l","mr--n1-l","mr--n2-l","mr--n3-l","mr--n4-l","mr--n5-l","mr--n6-l","mr--n7-l","mr--n8-l","mb--0","mb--1","mb--2","mb--3","mb--4","mb--5","mb--6","mb--7","mb--8","mb--n1","mb--n2","mb--n3","mb--n4","mb--n5","mb--n6","mb--n7","mb--n8","mb--0-s","mb--1-s","mb--2-s","mb--3-s","mb--4-s","mb--5-s","mb--6-s","mb--7-s","mb--8-s","mb--n1-s","mb--n2-s","mb--n3-s","mb--n4-s","mb--n5-s","mb--n6-s","mb--n7-s","mb--n8-s","mb--0-m","mb--1-m","mb--2-m","mb--3-m","mb--4-m","mb--5-m","mb--6-m","mb--7-m","mb--8-m","mb--n1-m","mb--n2-m","mb--n3-m","mb--n4-m","mb--n5-m","mb--n6-m","mb--n7-m","mb--n8-m","mb--0-l","mb--1-l","mb--2-l","mb--3-l","mb--4-l","mb--5-l","mb--6-l","mb--7-l","mb--8-l","mb--n1-l","mb--n2-l","mb--n3-l","mb--n4-l","mb--n5-l","mb--n6-l","mb--n7-l","mb--n8-l","ml--a","ml--0","ml--1","ml--2","ml--3","ml--4","ml--5","ml--6","ml--7","ml--8","ml--n1","ml--n2","ml--n3","ml--n4","ml--n5","ml--n6","ml--n7","ml--n8","ml--a-s","ml--0-s","ml--1-s","ml--2-s","ml--3-s","ml--4-s","ml--5-s","ml--6-s","ml--7-s","ml--8-s","ml--n1-s","ml--n2-s","ml--n3-s","ml--n4-s","ml--n5-s","ml--n6-s","ml--n7-s","ml--n8-s","ml--a-m","ml--0-m","ml--1-m","ml--2-m","ml--3-m","ml--4-m","ml--5-m","ml--6-m","ml--7-m","ml--8-m","ml--n1-m","ml--n2-m","ml--n3-m","ml--n4-m","ml--n5-m","ml--n6-m","ml--n7-m","ml--n8-m","ml--a-l","ml--0-l","ml--1-l","ml--2-l","ml--3-l","ml--4-l","ml--5-l","ml--6-l","ml--7-l","ml--8-l","ml--n1-l","ml--n2-l","ml--n3-l","ml--n4-l","ml--n5-l","ml--n6-l","ml--n7-l","ml--n8-l","my--0","my--1","my--2","my--3","my--4","my--5","my--6","my--7","my--8","my--n1","my--n2","my--n3","my--n4","my--n5","my--n6","my--n7","my--n8","my--0-s","my--1-s","my--2-s","my--3-s","my--4-s","my--5-s","my--6-s","my--7-s","my--8-s","my--n1-s","my--n2-s","my--n3-s","my--n4-s","my--n5-s","my--n6-s","my--n7-s","my--n8-s","my--0-m","my--1-m","my--2-m","my--3-m","my--4-m","my--5-m","my--6-m","my--7-m","my--8-m","my--n1-m","my--n2-m","my--n3-m","my--n4-m","my--n5-m","my--n6-m","my--n7-m","my--n8-m","my--0-l","my--1-l","my--2-l","my--3-l","my--4-l","my--5-l","my--6-l","my--7-l","my--8-l","my--n1-l","my--n2-l","my--n3-l","my--n4-l","my--n5-l","my--n6-l","my--n7-l","my--n8-l","mx--a","mx--0","mx--1","mx--2","mx--3","mx--4","mx--5","mx--6","mx--7","mx--8","mx--n1","mx--n2","mx--n3","mx--n4","mx--n5","mx--n6","mx--n7","mx--n8","mx--a-s","mx--0-s","mx--1-s","mx--2-s","mx--3-s","mx--4-s","mx--5-s","mx--6-s","mx--7-s","mx--8-s","mx--n1-s","mx--n2-s","mx--n3-s","mx--n4-s","mx--n5-s","mx--n6-s","mx--n7-s","mx--n8-s","mx--a-m","mx--0-m","mx--1-m","mx--2-m","mx--3-m","mx--4-m","mx--5-m","mx--6-m","mx--7-m","mx--8-m","mx--n1-m","mx--n2-m","mx--n3-m","mx--n4-m","mx--n5-m","mx--n6-m","mx--n7-m","mx--n8-m","mx--a-l","mx--0-l","mx--1-l","mx--2-l","mx--3-l","mx--4-l","mx--5-l","mx--6-l","mx--7-l","mx--8-l","mx--n1-l","mx--n2-l","mx--n3-l","mx--n4-l","mx--n5-l","mx--n6-l","mx--n7-l","mx--n8-l","ol--0","ol--0-s","ol--0-m","ol--0-l","brdrw--0","brdrw--1","brdrw--2","brdrw--3","brdrw--4","brdrw--5","brdrw--6","brdrw--7","brdrw--8","brdrtw--0","brdrtw--1","brdrtw--2","brdrtw--3","brdrtw--4","brdrtw--5","brdrtw--6","brdrtw--7","brdrtw--8","brdrrw--0","brdrrw--1","brdrrw--2","brdrrw--3","brdrrw--4","brdrrw--5","brdrrw--6","brdrrw--7","brdrrw--8","brdrbw--0","brdrbw--1","brdrbw--2","brdrbw--3","brdrbw--4","brdrbw--5","brdrbw--6","brdrbw--7","brdrbw--8","brdrlw--0","brdrlw--1","brdrlw--2","brdrlw--3","brdrlw--4","brdrlw--5","brdrlw--6","brdrlw--7","brdrlw--8","brdrw--0-s","brdrw--1-s","brdrw--2-s","brdrw--3-s","brdrw--4-s","brdrw--5-s","brdrw--6-s","brdrw--7-s","brdrw--8-s","brdrtw--0-s","brdrtw--1-s","brdrtw--2-s","brdrtw--3-s","brdrtw--4-s","brdrtw--5-s","brdrtw--6-s","brdrtw--7-s","brdrtw--8-s","brdrrw--0-s","brdrrw--1-s","brdrrw--2-s","brdrrw--3-s","brdrrw--4-s","brdrrw--5-s","brdrrw--6-s","brdrrw--7-s","brdrrw--8-s","brdrbw--0-s","brdrbw--1-s","brdrbw--2-s","brdrbw--3-s","brdrbw--4-s","brdrbw--5-s","brdrbw--6-s","brdrbw--7-s","brdrbw--8-s","brdrlw--0-s","brdrlw--1-s","brdrlw--2-s","brdrlw--3-s","brdrlw--4-s","brdrlw--5-s","brdrlw--6-s","brdrlw--7-s","brdrlw--8-s","brdrw--0-m","brdrw--1-m","brdrw--2-m","brdrw--3-m","brdrw--4-m","brdrw--5-m","brdrw--6-m","brdrw--7-m","brdrw--8-m","brdrtw--0-m","brdrtw--1-m","brdrtw--2-m","brdrtw--3-m","brdrtw--4-m","brdrtw--5-m","brdrtw--6-m","brdrtw--7-m","brdrtw--8-m","brdrrw--0-m","brdrrw--1-m","brdrrw--2-m","brdrrw--3-m","brdrrw--4-m","brdrrw--5-m","brdrrw--6-m","brdrrw--7-m","brdrrw--8-m","brdrbw--0-m","brdrbw--1-m","brdrbw--2-m","brdrbw--3-m","brdrbw--4-m","brdrbw--5-m","brdrbw--6-m","brdrbw--7-m","brdrbw--8-m","brdrlw--0-m","brdrlw--1-m","brdrlw--2-m","brdrlw--3-m","brdrlw--4-m","brdrlw--5-m","brdrlw--6-m","brdrlw--7-m","brdrlw--8-m","brdrw--0-l","brdrw--1-l","brdrw--2-l","brdrw--3-l","brdrw--4-l","brdrw--5-l","brdrw--6-l","brdrw--7-l","brdrw--8-l","brdrtw--0-l","brdrtw--1-l","brdrtw--2-l","brdrtw--3-l","brdrtw--4-l","brdrtw--5-l","brdrtw--6-l","brdrtw--7-l","brdrtw--8-l","brdrrw--0-l","brdrrw--1-l","brdrrw--2-l","brdrrw--3-l","brdrrw--4-l","brdrrw--5-l","brdrrw--6-l","brdrrw--7-l","brdrrw--8-l","brdrbw--0-l","brdrbw--1-l","brdrbw--2-l","brdrbw--3-l","brdrbw--4-l","brdrbw--5-l","brdrbw--6-l","brdrbw--7-l","brdrbw--8-l","brdrlw--0-l","brdrlw--1-l","brdrlw--2-l","brdrlw--3-l","brdrlw--4-l","brdrlw--5-l","brdrlw--6-l","brdrlw--7-l","brdrlw--8-l","brdrsty--das","brdrsty--dot","brdrsty--n","brdrsty--sol","brdrtsty--das","brdrtsty--dot","brdrtsty--n","brdrtsty--sol","brdrrsty--das","brdrrsty--dot","brdrrsty--n","brdrrsty--sol","brdrbsty--das","brdrbsty--dot","brdrbsty--n","brdrbsty--sol","brdrlsty--das","brdrlsty--dot","brdrlsty--n","brdrlsty--sol","brdrsty--das-s","brdrsty--dot-s","brdrsty--n-s","brdrsty--sol-s","brdrtsty--das-s","brdrtsty--dot-s","brdrtsty--n-s","brdrtsty--sol-s","brdrrsty--das-s","brdrrsty--dot-s","brdrrsty--n-s","brdrrsty--sol-s","brdrbsty--das-s","brdrbsty--dot-s","brdrbsty--n-s","brdrbsty--sol-s","brdrlsty--das-s","brdrlsty--dot-s","brdrlsty--n-s","brdrlsty--sol-s","brdrsty--das-m","brdrsty--dot-m","brdrsty--n-m","brdrsty--sol-m","brdrtsty--das-m","brdrtsty--dot-m","brdrtsty--n-m","brdrtsty--sol-m","brdrrsty--das-m","brdrrsty--dot-m","brdrrsty--n-m","brdrrsty--sol-m","brdrbsty--das-m","brdrbsty--dot-m","brdrbsty--n-m","brdrbsty--sol-m","brdrlsty--das-m","brdrlsty--dot-m","brdrlsty--n-m","brdrlsty--sol-m","brdrsty--das-l","brdrsty--dot-l","brdrsty--n-l","brdrsty--sol-l","brdrtsty--das-l","brdrtsty--dot-l","brdrtsty--n-l","brdrtsty--sol-l","brdrrsty--das-l","brdrrsty--dot-l","brdrrsty--n-l","brdrrsty--sol-l","brdrbsty--das-l","brdrbsty--dot-l","brdrbsty--n-l","brdrbsty--sol-l","brdrlsty--das-l","brdrlsty--dot-l","brdrlsty--n-l","brdrlsty--sol-l","brdrrad--0","brdrrad--1","brdrrad--2","brdrrad--3","brdrrad--4","brdrrad--5","brdrrad--6","brdrrad--7","brdrrad--8","brdrrad--100p","brdrtrrad--0","brdrtlrad--0","brdrbrrad--0","brdrblrad--0","brdrtrrad--1","brdrtlrad--1","brdrbrrad--1","brdrblrad--1","brdrtrrad--2","brdrtlrad--2","brdrbrrad--2","brdrblrad--2","brdrtrrad--3","brdrtlrad--3","brdrbrrad--3","brdrblrad--3","brdrtrrad--4","brdrtlrad--4","brdrbrrad--4","brdrblrad--4","brdrtrrad--5","brdrtlrad--5","brdrbrrad--5","brdrblrad--5","brdrtrrad--6","brdrtlrad--6","brdrbrrad--6","brdrblrad--6","brdrtrrad--7","brdrtlrad--7","brdrbrrad--7","brdrblrad--7","brdrtrrad--8","brdrtlrad--8","brdrbrrad--8","brdrblrad--8","brdrrad--0-s","brdrrad--1-s","brdrrad--2-s","brdrrad--3-s","brdrrad--4-s","brdrrad--5-s","brdrrad--6-s","brdrrad--7-s","brdrrad--8-s","brdrrad--100p-s","brdrtrrad--0-s","brdrtlrad--0-s","brdrbrrad--0-s","brdrblrad--0-s","brdrtrrad--1-s","brdrtlrad--1-s","brdrbrrad--1-s","brdrblrad--1-s","brdrtrrad--2-s","brdrtlrad--2-s","brdrbrrad--2-s","brdrblrad--2-s","brdrtrrad--3-s","brdrtlrad--3-s","brdrbrrad--3-s","brdrblrad--3-s","brdrtrrad--4-s","brdrtlrad--4-s","brdrbrrad--4-s","brdrblrad--4-s","brdrtrrad--5-s","brdrtlrad--5-s","brdrbrrad--5-s","brdrblrad--5-s","brdrtrrad--6-s","brdrtlrad--6-s","brdrbrrad--6-s","brdrblrad--6-s","brdrtrrad--7-s","brdrtlrad--7-s","brdrbrrad--7-s","brdrblrad--7-s","brdrtrrad--8-s","brdrtlrad--8-s","brdrbrrad--8-s","brdrblrad--8-s","brdrrad--0-m","brdrrad--1-m","brdrrad--2-m","brdrrad--3-m","brdrrad--4-m","brdrrad--5-m","brdrrad--6-m","brdrrad--7-m","brdrrad--8-m","brdrrad--100p-m","brdrtrrad--0-m","brdrtlrad--0-m","brdrbrrad--0-m","brdrblrad--0-m","brdrtrrad--1-m","brdrtlrad--1-m","brdrbrrad--1-m","brdrblrad--1-m","brdrtrrad--2-m","brdrtlrad--2-m","brdrbrrad--2-m","brdrblrad--2-m","brdrtrrad--3-m","brdrtlrad--3-m","brdrbrrad--3-m","brdrblrad--3-m","brdrtrrad--4-m","brdrtlrad--4-m","brdrbrrad--4-m","brdrblrad--4-m","brdrtrrad--5-m","brdrtlrad--5-m","brdrbrrad--5-m","brdrblrad--5-m","brdrtrrad--6-m","brdrtlrad--6-m","brdrbrrad--6-m","brdrblrad--6-m","brdrtrrad--7-m","brdrtlrad--7-m","brdrbrrad--7-m","brdrblrad--7-m","brdrtrrad--8-m","brdrtlrad--8-m","brdrbrrad--8-m","brdrblrad--8-m","brdrrad--0-l","brdrrad--1-l","brdrrad--2-l","brdrrad--3-l","brdrrad--4-l","brdrrad--5-l","brdrrad--6-l","brdrrad--7-l","brdrrad--8-l","brdrrad--100p-l","brdrtrrad--0-l","brdrtlrad--0-l","brdrbrrad--0-l","brdrblrad--0-l","brdrtrrad--1-l","brdrtlrad--1-l","brdrbrrad--1-l","brdrblrad--1-l","brdrtrrad--2-l","brdrtlrad--2-l","brdrbrrad--2-l","brdrblrad--2-l","brdrtrrad--3-l","brdrtlrad--3-l","brdrbrrad--3-l","brdrblrad--3-l","brdrtrrad--4-l","brdrtlrad--4-l","brdrbrrad--4-l","brdrblrad--4-l","brdrtrrad--5-l","brdrtlrad--5-l","brdrbrrad--5-l","brdrblrad--5-l","brdrtrrad--6-l","brdrtlrad--6-l","brdrbrrad--6-l","brdrblrad--6-l","brdrtrrad--7-l","brdrtlrad--7-l","brdrbrrad--7-l","brdrblrad--7-l","brdrtrrad--8-l","brdrtlrad--8-l","brdrbrrad--8-l","brdrblrad--8-l","brdrc--gy1","brdrc--gy2","brdrc--gy3","brdrc--gy4","brdrc--gy5","brdrc--gy6","brdrc--gy7","brdrc--gy8","brdrc--rd1","brdrc--gn1","brdrc--bl1","brdrc--yl1","brdrc--bk1","brdrc--wt1","brdrc--i","brdrc--tp","brdrtc--gy1","brdrtc--gy2","brdrtc--gy3","brdrtc--gy4","brdrtc--gy5","brdrtc--gy6","brdrtc--gy7","brdrtc--gy8","brdrtc--rd1","brdrtc--gn1","brdrtc--bl1","brdrtc--yl1","brdrtc--bk1","brdrtc--wt1","brdrtc--i","brdrtc--tp","brdrrc--gy1","brdrrc--gy2","brdrrc--gy3","brdrrc--gy4","brdrrc--gy5","brdrrc--gy6","brdrrc--gy7","brdrrc--gy8","brdrrc--rd1","brdrrc--gn1","brdrrc--bl1","brdrrc--yl1","brdrrc--bk1","brdrrc--wt1","brdrrc--i","brdrrc--tp","brdrbc--gy1","brdrbc--gy2","brdrbc--gy3","brdrbc--gy4","brdrbc--gy5","brdrbc--gy6","brdrbc--gy7","brdrbc--gy8","brdrbc--rd1","brdrbc--gn1","brdrbc--bl1","brdrbc--yl1","brdrbc--bk1","brdrbc--wt1","brdrbc--i","brdrbc--tp","brdrlc--gy1","brdrlc--gy2","brdrlc--gy3","brdrlc--gy4","brdrlc--gy5","brdrlc--gy6","brdrlc--gy7","brdrlc--gy8","brdrlc--rd1","brdrlc--gn1","brdrlc--bl1","brdrlc--yl1","brdrlc--bk1","brdrlc--wt1","brdrlc--i","brdrlc--tp","brdrc--gy1-s","brdrc--gy2-s","brdrc--gy3-s","brdrc--gy4-s","brdrc--gy5-s","brdrc--gy6-s","brdrc--gy7-s","brdrc--gy8-s","brdrc--rd1-s","brdrc--gn1-s","brdrc--bl1-s","brdrc--yl1-s","brdrc--bk1-s","brdrc--wt1-s","brdrc--i-s","brdrc--tp-s","brdrtc--gy1-s","brdrtc--gy2-s","brdrtc--gy3-s","brdrtc--gy4-s","brdrtc--gy5-s","brdrtc--gy6-s","brdrtc--gy7-s","brdrtc--gy8-s","brdrtc--rd1-s","brdrtc--gn1-s","brdrtc--bl1-s","brdrtc--yl1-s","brdrtc--bk1-s","brdrtc--wt1-s","brdrtc--i-s","brdrtc--tp-s","brdrrc--gy1-s","brdrrc--gy2-s","brdrrc--gy3-s","brdrrc--gy4-s","brdrrc--gy5-s","brdrrc--gy6-s","brdrrc--gy7-s","brdrrc--gy8-s","brdrrc--rd1-s","brdrrc--gn1-s","brdrrc--bl1-s","brdrrc--yl1-s","brdrrc--bk1-s","brdrrc--wt1-s","brdrrc--i-s","brdrrc--tp-s","brdrbc--gy1-s","brdrbc--gy2-s","brdrbc--gy3-s","brdrbc--gy4-s","brdrbc--gy5-s","brdrbc--gy6-s","brdrbc--gy7-s","brdrbc--gy8-s","brdrbc--rd1-s","brdrbc--gn1-s","brdrbc--bl1-s","brdrbc--yl1-s","brdrbc--bk1-s","brdrbc--wt1-s","brdrbc--i-s","brdrbc--tp-s","brdrlc--gy1-s","brdrlc--gy2-s","brdrlc--gy3-s","brdrlc--gy4-s","brdrlc--gy5-s","brdrlc--gy6-s","brdrlc--gy7-s","brdrlc--gy8-s","brdrlc--rd1-s","brdrlc--gn1-s","brdrlc--bl1-s","brdrlc--yl1-s","brdrlc--bk1-s","brdrlc--wt1-s","brdrlc--i-s","brdrlc--tp-s","brdrc--gy1-m","brdrc--gy2-m","brdrc--gy3-m","brdrc--gy4-m","brdrc--gy5-m","brdrc--gy6-m","brdrc--gy7-m","brdrc--gy8-m","brdrc--rd1-m","brdrc--gn1-m","brdrc--bl1-m","brdrc--yl1-m","brdrc--bk1-m","brdrc--wt1-m","brdrc--i-m","brdrc--tp-m","brdrtc--gy1-m","brdrtc--gy2-m","brdrtc--gy3-m","brdrtc--gy4-m","brdrtc--gy5-m","brdrtc--gy6-m","brdrtc--gy7-m","brdrtc--gy8-m","brdrtc--rd1-m","brdrtc--gn1-m","brdrtc--bl1-m","brdrtc--yl1-m","brdrtc--bk1-m","brdrtc--wt1-m","brdrtc--i-m","brdrtc--tp-m","brdrrc--gy1-m","brdrrc--gy2-m","brdrrc--gy3-m","brdrrc--gy4-m","brdrrc--gy5-m","brdrrc--gy6-m","brdrrc--gy7-m","brdrrc--gy8-m","brdrrc--rd1-m","brdrrc--gn1-m","brdrrc--bl1-m","brdrrc--yl1-m","brdrrc--bk1-m","brdrrc--wt1-m","brdrrc--i-m","brdrrc--tp-m","brdrbc--gy1-m","brdrbc--gy2-m","brdrbc--gy3-m","brdrbc--gy4-m","brdrbc--gy5-m","brdrbc--gy6-m","brdrbc--gy7-m","brdrbc--gy8-m","brdrbc--rd1-m","brdrbc--gn1-m","brdrbc--bl1-m","brdrbc--yl1-m","brdrbc--bk1-m","brdrbc--wt1-m","brdrbc--i-m","brdrbc--tp-m","brdrlc--gy1-m","brdrlc--gy2-m","brdrlc--gy3-m","brdrlc--gy4-m","brdrlc--gy5-m","brdrlc--gy6-m","brdrlc--gy7-m","brdrlc--gy8-m","brdrlc--rd1-m","brdrlc--gn1-m","brdrlc--bl1-m","brdrlc--yl1-m","brdrlc--bk1-m","brdrlc--wt1-m","brdrlc--i-m","brdrlc--tp-m","brdrc--gy1-l","brdrc--gy2-l","brdrc--gy3-l","brdrc--gy4-l","brdrc--gy5-l","brdrc--gy6-l","brdrc--gy7-l","brdrc--gy8-l","brdrc--rd1-l","brdrc--gn1-l","brdrc--bl1-l","brdrc--yl1-l","brdrc--bk1-l","brdrc--wt1-l","brdrc--i-l","brdrc--tp-l","brdrtc--gy1-l","brdrtc--gy2-l","brdrtc--gy3-l","brdrtc--gy4-l","brdrtc--gy5-l","brdrtc--gy6-l","brdrtc--gy7-l","brdrtc--gy8-l","brdrtc--rd1-l","brdrtc--gn1-l","brdrtc--bl1-l","brdrtc--yl1-l","brdrtc--bk1-l","brdrtc--wt1-l","brdrtc--i-l","brdrtc--tp-l","brdrrc--gy1-l","brdrrc--gy2-l","brdrrc--gy3-l","brdrrc--gy4-l","brdrrc--gy5-l","brdrrc--gy6-l","brdrrc--gy7-l","brdrrc--gy8-l","brdrrc--rd1-l","brdrrc--gn1-l","brdrrc--bl1-l","brdrrc--yl1-l","brdrrc--bk1-l","brdrrc--wt1-l","brdrrc--i-l","brdrrc--tp-l","brdrbc--gy1-l","brdrbc--gy2-l","brdrbc--gy3-l","brdrbc--gy4-l","brdrbc--gy5-l","brdrbc--gy6-l","brdrbc--gy7-l","brdrbc--gy8-l","brdrbc--rd1-l","brdrbc--gn1-l","brdrbc--bl1-l","brdrbc--yl1-l","brdrbc--bk1-l","brdrbc--wt1-l","brdrbc--i-l","brdrbc--tp-l","brdrlc--gy1-l","brdrlc--gy2-l","brdrlc--gy3-l","brdrlc--gy4-l","brdrlc--gy5-l","brdrlc--gy6-l","brdrlc--gy7-l","brdrlc--gy8-l","brdrlc--rd1-l","brdrlc--gn1-l","brdrlc--bl1-l","brdrlc--yl1-l","brdrlc--bk1-l","brdrlc--wt1-l","brdrlc--i-l","brdrlc--tp-l","bxsw--1","bxsw--2","bxsw--3","bxsw--4","bxsw--5","bxsw--1-s","bxsw--2-s","bxsw--3-s","bxsw--4-s","bxsw--5-s","bxsw--1-m","bxsw--2-m","bxsw--3-m","bxsw--4-m","bxsw--5-m","bxsw--1-l","bxsw--2-l","bxsw--3-l","bxsw--4-l","bxsw--5-l","bgc--gy1","bgc--gy2","bgc--gy3","bgc--gy4","bgc--gy5","bgc--gy6","bgc--gy7","bgc--gy8","bgc--rd1","bgc--gn1","bgc--bl1","bgc--yl1","bgc--bk1","bgc--wt1","bgc--i","bgc--currc","bgc--tp","bgc--gy1-s","bgc--gy2-s","bgc--gy3-s","bgc--gy4-s","bgc--gy5-s","bgc--gy6-s","bgc--gy7-s","bgc--gy8-s","bgc--rd1-s","bgc--gn1-s","bgc--bl1-s","bgc--yl1-s","bgc--bk1-s","bgc--wt1-s","bgc--i-s","bgc--currc-s","bgc--tp-s","bgc--gy1-m","bgc--gy2-m","bgc--gy3-m","bgc--gy4-m","bgc--gy5-m","bgc--gy6-m","bgc--gy7-m","bgc--gy8-m","bgc--rd1-m","bgc--gn1-m","bgc--bl1-m","bgc--yl1-m","bgc--bk1-m","bgc--wt1-m","bgc--i-m","bgc--currc-m","bgc--tp-m","bgc--gy1-l","bgc--gy2-l","bgc--gy3-l","bgc--gy4-l","bgc--gy5-l","bgc--gy6-l","bgc--gy7-l","bgc--gy8-l","bgc--rd1-l","bgc--gn1-l","bgc--bl1-l","bgc--yl1-l","bgc--bk1-l","bgc--wt1-l","bgc--i-l","bgc--currc-l","bgc--tp-l","bgpos--t","bgpos--r","bgpos--b","bgpos--l","bgpos--ctr","bgpos--t-s","bgpos--r-s","bgpos--b-s","bgpos--l-s","bgpos--ctr-s","bgpos--t-m","bgpos--r-m","bgpos--b-m","bgpos--l-m","bgpos--ctr-m","bgpos--t-l","bgpos--r-l","bgpos--b-l","bgpos--l-l","bgpos--ctr-l","bgrpt--n","bgrpt--x","bgrpt--y","bgrpt--n-s","bgrpt--x-s","bgrpt--y-s","bgrpt--n-m","bgrpt--x-m","bgrpt--y-m","bgrpt--n-l","bgrpt--x-l","bgrpt--y-l","bgs--con","bgs--cov","bgs--con-s","bgs--cov-s","bgs--con-m","bgs--cov-m","bgs--con-l","bgs--cov-l","p--0","p--1","p--2","p--3","p--4","p--5","p--6","p--7","p--8","p--n1","p--n2","p--n3","p--n4","p--n5","p--n6","p--n7","p--n8","p--0-s","p--1-s","p--2-s","p--3-s","p--4-s","p--5-s","p--6-s","p--7-s","p--8-s","p--n1-s","p--n2-s","p--n3-s","p--n4-s","p--n5-s","p--n6-s","p--n7-s","p--n8-s","p--0-m","p--1-m","p--2-m","p--3-m","p--4-m","p--5-m","p--6-m","p--7-m","p--8-m","p--n1-m","p--n2-m","p--n3-m","p--n4-m","p--n5-m","p--n6-m","p--n7-m","p--n8-m","p--0-l","p--1-l","p--2-l","p--3-l","p--4-l","p--5-l","p--6-l","p--7-l","p--8-l","p--n1-l","p--n2-l","p--n3-l","p--n4-l","p--n5-l","p--n6-l","p--n7-l","p--n8-l","pt--0","pt--1","pt--2","pt--3","pt--4","pt--5","pt--6","pt--7","pt--8","pt--n1","pt--n2","pt--n3","pt--n4","pt--n5","pt--n6","pt--n7","pt--n8","pt--0-s","pt--1-s","pt--2-s","pt--3-s","pt--4-s","pt--5-s","pt--6-s","pt--7-s","pt--8-s","pt--n1-s","pt--n2-s","pt--n3-s","pt--n4-s","pt--n5-s","pt--n6-s","pt--n7-s","pt--n8-s","pt--0-m","pt--1-m","pt--2-m","pt--3-m","pt--4-m","pt--5-m","pt--6-m","pt--7-m","pt--8-m","pt--n1-m","pt--n2-m","pt--n3-m","pt--n4-m","pt--n5-m","pt--n6-m","pt--n7-m","pt--n8-m","pt--0-l","pt--1-l","pt--2-l","pt--3-l","pt--4-l","pt--5-l","pt--6-l","pt--7-l","pt--8-l","pt--n1-l","pt--n2-l","pt--n3-l","pt--n4-l","pt--n5-l","pt--n6-l","pt--n7-l","pt--n8-l","pr--0","pr--1","pr--2","pr--3","pr--4","pr--5","pr--6","pr--7","pr--8","pr--n1","pr--n2","pr--n3","pr--n4","pr--n5","pr--n6","pr--n7","pr--n8","pr--0-s","pr--1-s","pr--2-s","pr--3-s","pr--4-s","pr--5-s","pr--6-s","pr--7-s","pr--8-s","pr--n1-s","pr--n2-s","pr--n3-s","pr--n4-s","pr--n5-s","pr--n6-s","pr--n7-s","pr--n8-s","pr--0-m","pr--1-m","pr--2-m","pr--3-m","pr--4-m","pr--5-m","pr--6-m","pr--7-m","pr--8-m","pr--n1-m","pr--n2-m","pr--n3-m","pr--n4-m","pr--n5-m","pr--n6-m","pr--n7-m","pr--n8-m","pr--0-l","pr--1-l","pr--2-l","pr--3-l","pr--4-l","pr--5-l","pr--6-l","pr--7-l","pr--8-l","pr--n1-l","pr--n2-l","pr--n3-l","pr--n4-l","pr--n5-l","pr--n6-l","pr--n7-l","pr--n8-l","pb--0","pb--1","pb--2","pb--3","pb--4","pb--5","pb--6","pb--7","pb--8","pb--n1","pb--n2","pb--n3","pb--n4","pb--n5","pb--n6","pb--n7","pb--n8","pb--0-s","pb--1-s","pb--2-s","pb--3-s","pb--4-s","pb--5-s","pb--6-s","pb--7-s","pb--8-s","pb--n1-s","pb--n2-s","pb--n3-s","pb--n4-s","pb--n5-s","pb--n6-s","pb--n7-s","pb--n8-s","pb--0-m","pb--1-m","pb--2-m","pb--3-m","pb--4-m","pb--5-m","pb--6-m","pb--7-m","pb--8-m","pb--n1-m","pb--n2-m","pb--n3-m","pb--n4-m","pb--n5-m","pb--n6-m","pb--n7-m","pb--n8-m","pb--0-l","pb--1-l","pb--2-l","pb--3-l","pb--4-l","pb--5-l","pb--6-l","pb--7-l","pb--8-l","pb--n1-l","pb--n2-l","pb--n3-l","pb--n4-l","pb--n5-l","pb--n6-l","pb--n7-l","pb--n8-l","pl--0","pl--1","pl--2","pl--3","pl--4","pl--5","pl--6","pl--7","pl--8","pl--n1","pl--n2","pl--n3","pl--n4","pl--n5","pl--n6","pl--n7","pl--n8","pl--0-s","pl--1-s","pl--2-s","pl--3-s","pl--4-s","pl--5-s","pl--6-s","pl--7-s","pl--8-s","pl--n1-s","pl--n2-s","pl--n3-s","pl--n4-s","pl--n5-s","pl--n6-s","pl--n7-s","pl--n8-s","pl--0-m","pl--1-m","pl--2-m","pl--3-m","pl--4-m","pl--5-m","pl--6-m","pl--7-m","pl--8-m","pl--n1-m","pl--n2-m","pl--n3-m","pl--n4-m","pl--n5-m","pl--n6-m","pl--n7-m","pl--n8-m","pl--0-l","pl--1-l","pl--2-l","pl--3-l","pl--4-l","pl--5-l","pl--6-l","pl--7-l","pl--8-l","pl--n1-l","pl--n2-l","pl--n3-l","pl--n4-l","pl--n5-l","pl--n6-l","pl--n7-l","pl--n8-l","py--0","py--1","py--2","py--3","py--4","py--5","py--6","py--7","py--8","py--n1","py--n2","py--n3","py--n4","py--n5","py--n6","py--n7","py--n8","py--0-s","py--1-s","py--2-s","py--3-s","py--4-s","py--5-s","py--6-s","py--7-s","py--8-s","py--n1-s","py--n2-s","py--n3-s","py--n4-s","py--n5-s","py--n6-s","py--n7-s","py--n8-s","py--0-m","py--1-m","py--2-m","py--3-m","py--4-m","py--5-m","py--6-m","py--7-m","py--8-m","py--n1-m","py--n2-m","py--n3-m","py--n4-m","py--n5-m","py--n6-m","py--n7-m","py--n8-m","py--0-l","py--1-l","py--2-l","py--3-l","py--4-l","py--5-l","py--6-l","py--7-l","py--8-l","py--n1-l","py--n2-l","py--n3-l","py--n4-l","py--n5-l","py--n6-l","py--n7-l","py--n8-l","px--0","px--1","px--2","px--3","px--4","px--5","px--6","px--7","px--8","px--n1","px--n2","px--n3","px--n4","px--n5","px--n6","px--n7","px--n8","px--0-s","px--1-s","px--2-s","px--3-s","px--4-s","px--5-s","px--6-s","px--7-s","px--8-s","px--n1-s","px--n2-s","px--n3-s","px--n4-s","px--n5-s","px--n6-s","px--n7-s","px--n8-s","px--0-m","px--1-m","px--2-m","px--3-m","px--4-m","px--5-m","px--6-m","px--7-m","px--8-m","px--n1-m","px--n2-m","px--n3-m","px--n4-m","px--n5-m","px--n6-m","px--n7-m","px--n8-m","px--0-l","px--1-l","px--2-l","px--3-l","px--4-l","px--5-l","px--6-l","px--7-l","px--8-l","px--n1-l","px--n2-l","px--n3-l","px--n4-l","px--n5-l","px--n6-l","px--n7-l","px--n8-l","w--a","w--1","w--2","w--3","w--4","w--5","w--6","w--7","w--8","w--10p","w--20p","w--25p","w--30p","w--33p","w--40p","w--50p","w--60p","w--66p","w--70p","w--75p","w--80p","w--90p","w--100p","w--a-s","w--1-s","w--2-s","w--3-s","w--4-s","w--5-s","w--6-s","w--7-s","w--8-s","w--10p-s","w--20p-s","w--25p-s","w--30p-s","w--33p-s","w--40p-s","w--50p-s","w--60p-s","w--66p-s","w--70p-s","w--75p-s","w--80p-s","w--90p-s","w--100p-s","w--a-m","w--1-m","w--2-m","w--3-m","w--4-m","w--5-m","w--6-m","w--7-m","w--8-m","w--10p-m","w--20p-m","w--25p-m","w--30p-m","w--33p-m","w--40p-m","w--50p-m","w--60p-m","w--66p-m","w--70p-m","w--75p-m","w--80p-m","w--90p-m","w--100p-m","w--a-l","w--1-l","w--2-l","w--3-l","w--4-l","w--5-l","w--6-l","w--7-l","w--8-l","w--10p-l","w--20p-l","w--25p-l","w--30p-l","w--33p-l","w--40p-l","w--50p-l","w--60p-l","w--66p-l","w--70p-l","w--75p-l","w--80p-l","w--90p-l","w--100p-l","miw--1","miw--2","miw--3","miw--4","miw--5","miw--6","miw--7","miw--8","miw--100p","miw--1-s","miw--2-s","miw--3-s","miw--4-s","miw--5-s","miw--6-s","miw--7-s","miw--8-s","miw--100p-s","miw--1-m","miw--2-m","miw--3-m","miw--4-m","miw--5-m","miw--6-m","miw--7-m","miw--8-m","miw--100p-m","miw--1-l","miw--2-l","miw--3-l","miw--4-l","miw--5-l","miw--6-l","miw--7-l","miw--8-l","miw--100p-l","maw--1","maw--2","maw--3","maw--4","maw--5","maw--6","maw--7","maw--8","maw--10p","maw--20p","maw--25p","maw--30p","maw--33p","maw--40p","maw--50p","maw--60p","maw--66p","maw--70p","maw--75p","maw--80p","maw--90p","maw--100p","maw--1-s","maw--2-s","maw--3-s","maw--4-s","maw--5-s","maw--6-s","maw--7-s","maw--8-s","maw--10p-s","maw--20p-s","maw--25p-s","maw--30p-s","maw--33p-s","maw--40p-s","maw--50p-s","maw--60p-s","maw--66p-s","maw--70p-s","maw--75p-s","maw--80p-s","maw--90p-s","maw--100p-s","maw--1-m","maw--2-m","maw--3-m","maw--4-m","maw--5-m","maw--6-m","maw--7-m","maw--8-m","maw--10p-m","maw--20p-m","maw--25p-m","maw--30p-m","maw--33p-m","maw--40p-m","maw--50p-m","maw--60p-m","maw--66p-m","maw--70p-m","maw--75p-m","maw--80p-m","maw--90p-m","maw--100p-m","maw--1-l","maw--2-l","maw--3-l","maw--4-l","maw--5-l","maw--6-l","maw--7-l","maw--8-l","maw--10p-l","maw--20p-l","maw--25p-l","maw--30p-l","maw--33p-l","maw--40p-l","maw--50p-l","maw--60p-l","maw--66p-l","maw--70p-l","maw--75p-l","maw--80p-l","maw--90p-l","maw--100p-l","h--a","h--1","h--2","h--3","h--4","h--5","h--6","h--7","h--8","h--100p","h--100vh","h--a-s","h--1-s","h--2-s","h--3-s","h--4-s","h--5-s","h--6-s","h--7-s","h--8-s","h--100p-s","h--100vh-s","h--a-m","h--1-m","h--2-m","h--3-m","h--4-m","h--5-m","h--6-m","h--7-m","h--8-m","h--100p-m","h--100vh-m","h--a-l","h--1-l","h--2-l","h--3-l","h--4-l","h--5-l","h--6-l","h--7-l","h--8-l","h--100p-l","h--100vh-l","mih--0","mih--100p","mih--100vh","mih--0-s","mih--100p-s","mih--100vh-s","mih--0-m","mih--100p-m","mih--100vh-m","mih--0-l","mih--100p-l","mih--100vh-l","mah--100p","mah--100vh","mah--100p-s","mah--100vh-s","mah--100p-m","mah--100vh-m","mah--100p-l","mah--100vh-l","of--a","of--hid","of--sl","of--v","ofx--a","ofx--hid","ofx--sl","ofx--v","ofy--a","ofy--hid","ofy--sl","ofy--v","of--a-s","of--hid-s","of--sl-s","of--v-s","ofx--a-s","ofx--hid-s","ofx--sl-s","ofx--v-s","ofy--a-s","ofy--hid-s","ofy--sl-s","ofy--v-s","of--a-m","of--hid-m","of--sl-m","of--v-m","ofx--a-m","ofx--hid-m","ofx--sl-m","ofx--v-m","ofy--a-m","ofy--hid-m","ofy--sl-m","ofy--v-m","of--a-l","of--hid-l","of--sl-l","of--v-l","ofx--a-l","ofx--hid-l","ofx--sl-l","ofx--v-l","ofy--a-l","ofy--hid-l","ofy--sl-l","ofy--v-l","re--bh","re--n","re--x","re--y","re--bh-s","re--n-s","re--x-s","re--y-s","re--bh-m","re--n-m","re--x-m","re--y-m","re--bh-l","re--n-l","re--x-l","re--y-l","lssty--ins","lssty--n","lssty--sq","lssty--ins-s","lssty--n-s","lssty--sq-s","lssty--ins-m","lssty--n-m","lssty--sq-m","lssty--ins-l","lssty--n-l","lssty--sq-l","tbllyt--a","tbllyt--fix","tbllyt-s--a","tbllyt-s--fix","tbllyt-m--a","tbllyt-m--fix","tbllyt-l--a","tbllyt-l--fix","brdrcolaps--colaps","brdrcolaps--sep","brdrcolaps--colaps-s","brdrcolaps--sep-s","brdrcolaps--colaps-m","brdrcolaps--sep-m","brdrcolaps--colaps-l","brdrcolaps--sep-l","brdrsp--0","brdrsp--1","brdrsp--2","brdrsp--3","brdrsp--4","brdrsp--5","brdrsp--6","brdrsp--7","brdrsp--8","brdrsp--0-s","brdrsp--1-s","brdrsp--2-s","brdrsp--3-s","brdrsp--4-s","brdrsp--5-s","brdrsp--6-s","brdrsp--7-s","brdrsp--8-s","brdrsp--0-m","brdrsp--1-m","brdrsp--2-m","brdrsp--3-m","brdrsp--4-m","brdrsp--5-m","brdrsp--6-m","brdrsp--7-m","brdrsp--8-m","brdrsp--0-l","brdrsp--1-l","brdrsp--2-l","brdrsp--3-l","brdrsp--4-l","brdrsp--5-l","brdrsp--6-l","brdrsp--7-l","brdrsp--8-l","vrtan--t","vrtan--b","vrtan--ble","vrtan--mid","vrtan--t-s","vrtan--b-s","vrtan--ble-s","vrtan--mid-s","vrtan--t-m","vrtan--b-m","vrtan--ble-m","vrtan--mid-m","vrtan--t-m","vrtan--b-m","vrtan--ble-l","vrtan--mid-l","dir--ltr","dir--rtl","dir--ltr-s","dir--rtl-s","dir--ltr-m","dir--rtl-m","dir--ltr-l","dir--rtl-l","txtan--r","txtan--l","txtan--ctr","txtan--j","txtan--r-s","txtan--l-s","txtan--ctr-s","txtan--j-s","txtan--r-m","txtan--l-m","txtan--ctr-m","txtan--j-m","txtan--r-l","txtan--l-l","txtan--ctr-l","txtan--j-l","txttr--cap","txttr--lc","txttr--n","txttr--uc","txttr--cap-s","txttr--lc-s","txttr--n-s","txttr--uc-s","txttr--cap-m","txttr--lc-m","txttr--n-m","txttr--uc-m","txttr--cap-l","txttr--lc-l","txttr--n-l","txttr--uc-l","txtdecor--n","txtdecor--u","txtdecor--n-s","txtdecor--u-s","txtdecor--n-m","txtdecor--u-m","txtdecor--n-l","txtdecor--u-l","lnh--0","lnh--1","lnh--2","lnh--3","lnh--4","lnh--5","lnh--6","lnh--7","lnh--8","lnh--0-s","lnh--1-s","lnh--2-s","lnh--3-s","lnh--4-s","lnh--5-s","lnh--6-s","lnh--7-s","lnh--8-s","lnh--0-m","lnh--1-m","lnh--2-m","lnh--3-m","lnh--4-m","lnh--5-m","lnh--6-m","lnh--7-m","lnh--8-m","lnh--0-l","lnh--1-l","lnh--2-l","lnh--3-l","lnh--4-l","lnh--5-l","lnh--6-l","lnh--7-l","lnh--8-l","wdsp--1","wdsp--2","wdsp--3","wdsp--4","wdsp--5","wdsp--6","wdsp--7","wdsp--8","wdsp--nl","wdsp--1-s","wdsp--2-s","wdsp--3-s","wdsp--4-s","wdsp--5-s","wdsp--6-s","wdsp--7-s","wdsp--8-s","wdsp--nl-s","wdsp--1-m","wdsp--2-m","wdsp--3-m","wdsp--4-m","wdsp--5-m","wdsp--6-m","wdsp--7-m","wdsp--8-m","wdsp--nl-m","wdsp--1-l","wdsp--2-l","wdsp--3-l","wdsp--4-l","wdsp--5-l","wdsp--6-l","wdsp--7-l","wdsp--8-l","wdsp--nl-l","ltrsp--1","ltrsp--n1","ltrsp--nl","ltrsp--1-s","ltrsp--n1-s","ltrsp--nl-s","ltrsp--1-m","ltrsp--n1-m","ltrsp--nl-m","ltrsp--1-l","ltrsp--n1-l","ltrsp--nl-l","wtsp--nl","wtsp--n","wtsp--pre","wtsp--nls","wtsp--n-s","wtsp--pre-s","wtsp--nl-m","wtsp--n-m","wtsp--pre-m","wtsp--nl-l","wtsp--n-l","wtsp--pre-l","wdwp--brwd","wdwp--nl","wdwp--brwd-s","wdwp--nl-s","wdwp--brwd-m","wdwp--nl-m","wdwp--brwd-l","wdwp--nl-l","c--gy1","c--gy2","c--gy3","c--gy4","c--gy5","c--gy6","c--gy7","c--gy8","c--rd1","c--gn1","c--bl1","c--yl1","c--bk1","c--wt1","c--tp","c--i","c--gy1-s","c--gy2-s","c--gy3-s","c--gy4-s","c--gy5-s","c--gy6-s","c--gy7-s","c--gy8-s","c--rd1-s","c--gn1-s","c--bl1-s","c--yl1-s","c--bk1-s","c--wt1-s","c--tp-s","c--i-s","c--gy1-m","c--gy2-m","c--gy3-m","c--gy4-m","c--gy5-m","c--gy6-m","c--gy7-m","c--gy8-m","c--rd1-m","c--gn1-m","c--bl1-m","c--yl1-m","c--bk1-m","c--wt1-m","c--tp-m","c--i-m","c--gy1-l","c--gy2-l","c--gy3-l","c--gy4-l","c--gy5-l","c--gy6-l","c--gy7-l","c--gy8-l","c--rd1-l","c--gn1-l","c--bl1-l","c--yl1-l","c--bk1-l","c--wt1-l","c--tp-l","c--i-l","fts--1","fts--2","fts--3","fts--4","fts--5","fts--6","fts--7","fts--8","fts--i","fts--1-s","fts--2-s","fts--3-s","fts--4-s","fts--5-s","fts--6-s","fts--7-s","fts--8-s","fts--i-s","fts--1-m","fts--2-m","fts--3-m","fts--4-m","fts--5-m","fts--6-m","fts--7-m","fts--8-m","fts--i-m","fts--1-l","fts--2-l","fts--3-l","fts--4-l","fts--5-l","fts--6-l","fts--7-l","fts--8-l","fts--i-l","ftwgt--1","ftwgt--2","ftwgt--3","ftwgt--4","ftwgt--5","ftwgt--6","ftwgt--7","ftwgt--8","ftwgt--1-s","ftwgt--2-s","ftwgt--3-s","ftwgt--4-s","ftwgt--5-s","ftwgt--6-s","ftwgt--7-s","ftwgt--8-s","ftwgt--1-m","ftwgt--2-m","ftwgt--3-m","ftwgt--4-m","ftwgt--5-m","ftwgt--6-m","ftwgt--7-m","ftwgt--8-m","ftwgt--1-l","ftwgt--2-l","ftwgt--3-l","ftwgt--4-l","ftwgt--5-l","ftwgt--6-l","ftwgt--7-l","ftwgt--8-l","ftsty--ic","ftsty--nl","ftsty--ic-s","ftsty--nl-s","ftsty--ic-m","ftsty--nl-m","ftsty--ic-l","ftsty--nl-l"]

class BrevisCompletions(sublime_plugin.EventListener):
	def __init__(self):
		
		self.class_completions = [("%s \tBrevis Class" % s, s) for s in brevis_classes]

	def on_query_completions(self, view, prefix, locations):
		
		if view.match_selector(locations[0], "text.html string.quoted"):

			# Cursor is inside a quoted attribute
			# Now check if we are inside the class attribute

			# max search size
			LIMIT  = 250

			# place search cursor one word back
			cursor = locations[0] - len(prefix) - 1

			# dont start with negative value
			start  = max(0, cursor - LIMIT - len(prefix))

			# get part of buffer
			line   = view.substr(sublime.Region(start, cursor))

			# split attributes
			parts = line.split('=')
			
			# is the last typed attribute a class attribute?
			if len(parts) > 1 and parts[-2].strip().endswith("class"):
				return self.class_completions
			else:
				return []
		elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

			# Cursor is in a tag, but not inside an attribute, i.e. <div {here}>
			return self.data_completions
			
		else:
			return []
