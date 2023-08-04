J$.iids = {"8":[10,5,10,16],"9":[2,10,2,17],"10":[10,5,10,16],"17":[2,18,2,22],"25":[2,10,2,23],"33":[2,10,2,23],"41":[2,10,2,23],"49":[5,12,5,14],"57":[5,22,5,33],"65":[5,35,5,39],"73":[5,12,5,40],"75":[5,12,5,21],"81":[5,12,5,40],"89":[5,12,5,40],"97":[6,11,6,13],"105":[6,21,6,30],"113":[6,32,6,36],"121":[6,11,6,37],"123":[6,11,6,20],"129":[6,11,6,37],"137":[6,11,6,37],"145":[10,5,10,9],"153":[10,13,10,16],"161":[11,9,11,14],"169":[11,9,11,14],"177":[11,3,11,15],"185":[14,9,14,13],"193":[14,9,14,13],"201":[14,3,14,14],"209":[1,1,15,2],"217":[1,1,15,2],"225":[1,1,15,2],"233":[1,1,15,2],"241":[10,1,15,2],"249":[1,1,15,2],"257":[1,1,15,2],"nBranches":2,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/mytest.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/mytest_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar high = S$.symbol('ucon_HIGH', true);\nvar low = S$.symbol('con_LOW', true);\n// var my_num = S$.symbol('my_num', 3);\n\n/* MAIN JS PROGRAM */\nif (high == low){\n  low = false\n}\nelse{\n  low = true\n}\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(209, '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/mytest_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/mytest.js');
            J$.N(217, 'S$', S$, 0);
            J$.N(225, 'high', high, 0);
            J$.N(233, 'low', low, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var high = J$.X1(89, J$.W(81, 'high', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_HIGH', 21, false), J$.T(65, true, 23, false)), high, 3));
            var low = J$.X1(137, J$.W(129, 'low', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_LOW', 21, false), J$.T(113, true, 23, false)), low, 3));
            if (J$.X1(241, J$.C(8, J$.B(10, '==', J$.R(145, 'high', high, 1), J$.R(153, 'low', low, 1), 0)))) {
                J$.X1(177, low = J$.W(169, 'low', J$.T(161, false, 23, false), low, 2));
            } else {
                J$.X1(201, low = J$.W(193, 'low', J$.T(185, true, 23, false), low, 2));
            }
        } catch (J$e) {
            J$.Ex(249, J$e);
        } finally {
            if (J$.Sr(257)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
