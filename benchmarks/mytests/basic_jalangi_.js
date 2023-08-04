J$.iids = {"8":[11,6,11,20],"9":[2,10,2,17],"10":[8,11,8,23],"16":[10,17,10,29],"17":[2,18,2,22],"18":[10,17,10,29],"25":[2,10,2,23],"26":[10,31,10,34],"33":[2,10,2,23],"41":[2,10,2,23],"42":[10,31,10,34],"49":[4,9,4,11],"50":[11,6,11,20],"57":[4,19,4,22],"65":[4,25,4,41],"73":[4,24,4,42],"81":[4,9,4,43],"83":[4,9,4,18],"89":[4,9,4,43],"97":[4,9,4,43],"105":[5,9,5,11],"113":[5,19,5,22],"121":[5,24,5,28],"129":[5,9,5,29],"131":[5,9,5,18],"137":[5,9,5,29],"145":[5,9,5,29],"153":[8,1,8,3],"161":[8,11,8,12],"169":[8,11,8,19],"177":[8,22,8,23],"185":[8,1,8,24],"187":[8,1,8,10],"193":[8,1,8,25],"201":[10,14,10,15],"209":[10,14,10,15],"217":[10,14,10,15],"225":[10,17,10,18],"233":[10,21,10,22],"241":[10,21,10,29],"257":[10,31,10,32],"265":[10,31,10,34],"281":[11,6,11,7],"289":[11,8,11,9],"297":[11,6,11,10],"305":[11,14,11,20],"313":[12,7,12,12],"321":[12,7,12,12],"329":[12,3,12,13],"337":[13,9,13,20],"345":[13,9,13,20],"353":[13,3,13,21],"361":[1,1,15,2],"369":[1,1,15,2],"377":[1,1,15,2],"385":[1,1,15,2],"393":[1,1,15,2],"401":[11,2,14,3],"409":[10,1,15,2],"417":[10,1,15,2],"425":[1,1,15,2],"433":[1,1,15,2],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/python/extract_symbolic/mytests/basic.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/python/extract_symbolic/mytests/basic_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\nvar x = S$.symbol('X', ['A,Ah,What,What']);\nvar y = S$.symbol('Y', true);\n\n// S$.assume(x.length < 4);\nS$.assert(x.length < 4);\n\nfor (var i=0; i < x.length; i++) {\n\tif (x[i] == 'What') {\n\t\ty = false\n\t\tthrow 'Reachable';\n\t}\n}\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(361, '/Users/tzuhan/+research/hyper_enforce/python/extract_symbolic/mytests/basic_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/python/extract_symbolic/mytests/basic.js');
            J$.N(369, 'S$', S$, 0);
            J$.N(377, 'x', x, 0);
            J$.N(385, 'y', y, 0);
            J$.N(393, 'i', i, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var x = J$.X1(97, J$.W(89, 'x', J$.M(81, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'X', 21, false), J$.T(73, [J$.T(65, 'A,Ah,What,What', 21, false)], 10, false)), x, 3));
            var y = J$.X1(145, J$.W(137, 'y', J$.M(129, J$.R(105, 'S$', S$, 1), 'symbol', 0)(J$.T(113, 'Y', 21, false), J$.T(121, true, 23, false)), y, 3));
            J$.X1(193, J$.M(185, J$.R(153, 'S$', S$, 1), 'assert', 0)(J$.B(10, '<', J$.G(169, J$.R(161, 'x', x, 1), 'length', 0), J$.T(177, 4, 22, false), 0)));
            for (var i = J$.X1(217, J$.W(209, 'i', J$.T(201, 0, 22, false), i, 3)); J$.X1(409, J$.C(16, J$.B(18, '<', J$.R(225, 'i', i, 1), J$.G(241, J$.R(233, 'x', x, 1), 'length', 0), 0))); J$.X1(417, J$.B(42, '-', i = J$.W(265, 'i', J$.B(34, '+', J$.U(26, '+', J$.R(257, 'i', i, 1)), J$.T(249, 1, 22, false), 0), i, 2), J$.T(273, 1, 22, false), 0))) {
                if (J$.X1(401, J$.C(8, J$.B(50, '==', J$.G(297, J$.R(281, 'x', x, 1), J$.R(289, 'i', i, 1), 4), J$.T(305, 'What', 21, false), 0)))) {
                    J$.X1(329, y = J$.W(321, 'y', J$.T(313, false, 23, false), y, 2));
                    throw J$.X1(353, J$.Th(345, J$.T(337, 'Reachable', 21, false)));
                }
            }
        } catch (J$e) {
            J$.Ex(425, J$e);
        } finally {
            if (J$.Sr(433)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
