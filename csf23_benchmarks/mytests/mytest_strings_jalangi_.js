J$.iids = {"8":[11,9,11,30],"9":[2,10,2,17],"10":[10,5,10,24],"16":[10,5,10,24],"17":[2,18,2,22],"18":[11,9,11,30],"24":[15,5,15,25],"25":[2,10,2,23],"26":[15,5,15,25],"33":[2,10,2,23],"41":[2,10,2,23],"49":[5,20,5,22],"57":[5,30,5,44],"65":[5,46,5,49],"73":[5,20,5,50],"75":[5,20,5,29],"81":[5,20,5,50],"89":[5,20,5,50],"97":[6,13,6,15],"105":[6,23,6,30],"113":[6,32,6,44],"121":[6,13,6,45],"123":[6,13,6,22],"129":[6,13,6,45],"137":[6,13,6,45],"145":[7,20,7,22],"153":[7,30,7,44],"161":[7,46,7,47],"169":[7,20,7,48],"171":[7,20,7,29],"177":[7,20,7,48],"185":[7,20,7,48],"193":[10,5,10,17],"201":[10,21,10,24],"209":[11,9,11,14],"217":[11,18,11,30],"225":[15,5,15,17],"233":[15,22,15,25],"241":[16,20,16,31],"249":[16,20,16,31],"257":[16,5,16,32],"265":[17,20,17,25],"273":[17,20,17,35],"275":[17,20,17,33],"281":[17,20,17,35],"289":[17,5,17,36],"297":[18,22,18,34],"305":[18,22,18,41],"313":[18,22,18,41],"321":[18,22,18,41],"329":[19,20,19,30],"337":[19,20,19,40],"339":[19,20,19,38],"345":[19,20,19,40],"353":[19,5,19,41],"361":[1,1,21,20],"369":[1,1,21,20],"377":[1,1,21,20],"385":[1,1,21,20],"393":[1,1,21,20],"401":[1,1,21,20],"409":[11,5,12,6],"417":[10,1,13,2],"425":[15,1,20,2],"433":[1,1,21,20],"441":[1,1,21,20],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest_strings.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest_strings_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\nvar S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar con_str_test = S$.symbol('con_str_test', 'a')\nvar value = S$.symbol('value', 'some_value')\nvar con_num_test = S$.symbol('con_num_test', 4)\n\n/* NECESSARY CONRETE TESTS */\nif ((con_str_test == 'a')) {\n  if (value == 'some_value'){\n  }\n}\n/* MAIN JS PROGRAM */\nif (con_str_test === 'a') {\n    con_str_test = 'cccdddeee'\n    con_str_test = value.valueOf()\n    var aux_length = con_str_test.length\n    con_num_test = aux_length.valueOf()\n}\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(361, '/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest_strings_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/model_builder/mytests/mytest_strings.js');
            J$.N(369, 'S$', S$, 0);
            J$.N(377, 'con_str_test', con_str_test, 0);
            J$.N(385, 'value', value, 0);
            J$.N(393, 'con_num_test', con_num_test, 0);
            J$.N(401, 'aux_length', aux_length, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_str_test = J$.X1(89, J$.W(81, 'con_str_test', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_str_test', 21, false), J$.T(65, 'a', 21, false)), con_str_test, 3));
            var value = J$.X1(137, J$.W(129, 'value', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'value', 21, false), J$.T(113, 'some_value', 21, false)), value, 3));
            var con_num_test = J$.X1(185, J$.W(177, 'con_num_test', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_num_test', 21, false), J$.T(161, 4, 22, false)), con_num_test, 3));
            if (J$.X1(417, J$.C(16, J$.B(10, '==', J$.R(193, 'con_str_test', con_str_test, 1), J$.T(201, 'a', 21, false), 0)))) {
                if (J$.X1(409, J$.C(8, J$.B(18, '==', J$.R(209, 'value', value, 1), J$.T(217, 'some_value', 21, false), 0)))) {
                }
            }
            if (J$.X1(425, J$.C(24, J$.B(26, '===', J$.R(225, 'con_str_test', con_str_test, 1), J$.T(233, 'a', 21, false), 0)))) {
                J$.X1(257, con_str_test = J$.W(249, 'con_str_test', J$.T(241, 'cccdddeee', 21, false), con_str_test, 2));
                J$.X1(289, con_str_test = J$.W(281, 'con_str_test', J$.M(273, J$.R(265, 'value', value, 1), 'valueOf', 0)(), con_str_test, 2));
                var aux_length = J$.X1(321, J$.W(313, 'aux_length', J$.G(305, J$.R(297, 'con_str_test', con_str_test, 1), 'length', 0), aux_length, 3));
                J$.X1(353, con_num_test = J$.W(345, 'con_num_test', J$.M(337, J$.R(329, 'aux_length', aux_length, 1), 'valueOf', 0)(), con_num_test, 2));
            }
        } catch (J$e) {
            J$.Ex(433, J$e);
        } finally {
            if (J$.Sr(441)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
