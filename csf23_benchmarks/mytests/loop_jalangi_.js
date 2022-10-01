J$.iids = {"8":[8,6,8,11],"9":[3,10,3,17],"10":[7,17,7,22],"16":[7,17,7,22],"17":[3,18,3,22],"18":[7,24,7,27],"25":[3,10,3,23],"33":[3,10,3,23],"34":[7,24,7,27],"41":[3,10,3,23],"42":[8,6,8,11],"49":[4,9,4,11],"50":[9,3,9,6],"57":[4,19,4,22],"65":[4,24,4,25],"66":[9,3,9,6],"73":[4,9,4,26],"74":[12,13,12,24],"75":[4,9,4,18],"81":[4,9,4,26],"89":[4,9,4,26],"97":[5,9,5,11],"105":[5,19,5,22],"113":[5,24,5,25],"121":[5,9,5,26],"123":[5,9,5,18],"129":[5,9,5,26],"137":[5,9,5,26],"145":[7,14,7,15],"153":[7,14,7,15],"161":[7,14,7,15],"169":[7,17,7,18],"177":[7,21,7,22],"193":[7,24,7,25],"201":[7,24,7,27],"217":[8,6,8,7],"225":[8,10,8,11],"241":[9,3,9,4],"249":[9,3,9,6],"265":[9,3,9,7],"273":[12,1,12,8],"281":[12,13,12,20],"289":[12,23,12,24],"297":[12,1,12,25],"299":[12,1,12,12],"305":[12,1,12,26],"313":[1,1,12,26],"321":[1,1,12,26],"329":[1,1,12,26],"337":[1,1,12,26],"345":[1,1,12,26],"353":[8,2,10,3],"361":[7,1,11,2],"369":[7,1,11,2],"377":[1,1,12,26],"385":[1,1,12,26],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/loop.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/loop_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\n\nvar S$ = require('S$');\nvar q = S$.symbol('Q', 3);\nvar j = S$.symbol('J', 0);\n\nfor (var i = 0; i < 2; i++) {\n\tif(i > 0){\n\t\t\tj++;\n\t}\n}\nconsole.log('Done ' + j);\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(313, '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/loop_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/loop.js');
            J$.N(321, 'S$', S$, 0);
            J$.N(329, 'q', q, 0);
            J$.N(337, 'j', j, 0);
            J$.N(345, 'i', i, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var q = J$.X1(89, J$.W(81, 'q', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'Q', 21, false), J$.T(65, 3, 22, false)), q, 3));
            var j = J$.X1(137, J$.W(129, 'j', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'J', 21, false), J$.T(113, 0, 22, false)), j, 3));
            for (var i = J$.X1(161, J$.W(153, 'i', J$.T(145, 0, 22, false), i, 3)); J$.X1(361, J$.C(16, J$.B(10, '<', J$.R(169, 'i', i, 1), J$.T(177, 2, 22, false), 0))); J$.X1(369, J$.B(34, '-', i = J$.W(201, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(193, 'i', i, 1)), J$.T(185, 1, 22, false), 0), i, 2), J$.T(209, 1, 22, false), 0))) {
                if (J$.X1(353, J$.C(8, J$.B(42, '>', J$.R(217, 'i', i, 1), J$.T(225, 0, 22, false), 0)))) {
                    J$.X1(265, J$.B(66, '-', j = J$.W(249, 'j', J$.B(58, '+', J$.U(50, '+', J$.R(241, 'j', j, 1)), J$.T(233, 1, 22, false), 0), j, 2), J$.T(257, 1, 22, false), 0));
                }
            }
            J$.X1(305, J$.M(297, J$.R(273, 'console', console, 2), 'log', 0)(J$.B(74, '+', J$.T(281, 'Done ', 21, false), J$.R(289, 'j', j, 1), 0)));
        } catch (J$e) {
            J$.Ex(377, J$e);
        } finally {
            if (J$.Sr(385)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
