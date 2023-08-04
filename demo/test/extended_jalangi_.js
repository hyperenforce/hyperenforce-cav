J$.iids = {"8":[13,7,13,30],"9":[1,10,1,17],"10":[12,13,12,19],"16":[12,13,12,19],"17":[1,18,1,22],"18":[12,21,12,24],"24":[28,5,28,12],"25":[1,10,1,23],"33":[1,10,1,23],"34":[12,21,12,24],"41":[1,10,1,23],"42":[13,7,13,30],"49":[4,26,4,28],"50":[23,18,23,59],"57":[4,36,4,56],"58":[27,22,27,63],"65":[4,58,4,60],"66":[28,5,28,12],"73":[4,26,4,61],"74":[29,19,29,36],"75":[4,26,4,35],"81":[4,26,4,61],"89":[4,26,4,61],"97":[5,21,5,23],"105":[5,31,5,46],"113":[5,48,5,49],"121":[5,21,5,50],"123":[5,21,5,30],"129":[5,21,5,50],"137":[5,21,5,50],"145":[6,28,6,30],"153":[6,38,6,60],"161":[6,62,6,63],"169":[6,28,6,64],"171":[6,28,6,37],"177":[6,28,6,64],"185":[6,28,6,64],"193":[7,14,7,16],"201":[7,24,7,32],"209":[7,34,7,38],"217":[7,14,7,39],"219":[7,14,7,23],"225":[7,14,7,39],"233":[7,14,7,39],"241":[8,22,8,24],"249":[8,32,8,48],"257":[8,50,8,51],"265":[8,22,8,52],"267":[8,22,8,31],"273":[8,22,8,52],"281":[8,22,8,52],"289":[11,9,11,10],"297":[11,9,11,10],"305":[11,9,11,10],"313":[12,10,12,11],"321":[12,10,12,11],"329":[12,13,12,14],"337":[12,17,12,19],"353":[12,21,12,22],"361":[12,21,12,24],"377":[13,7,13,25],"385":[13,29,13,30],"393":[23,18,23,36],"401":[23,39,23,59],"409":[23,18,23,59],"417":[23,1,23,60],"425":[27,22,27,40],"433":[27,43,27,63],"441":[27,22,27,63],"449":[27,1,27,64],"457":[28,6,28,12],"465":[29,19,29,32],"473":[29,35,29,36],"481":[29,19,29,36],"489":[29,3,29,37],"497":[1,1,35,21],"505":[1,1,35,21],"513":[1,1,35,21],"521":[1,1,35,21],"529":[1,1,35,21],"537":[1,1,35,21],"545":[1,1,35,21],"553":[1,1,35,21],"561":[1,1,35,21],"569":[13,3,13,34],"577":[12,1,14,2],"585":[12,1,14,2],"593":[12,1,14,2],"601":[28,1,30,2],"609":[1,1,35,21],"617":[1,1,35,21],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/test/extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/test/extended_jalangi_.js","code":"var S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_num_h_balance = S$.symbol('ucon_num_h_balance', 20);\nvar con_num_l_obs = S$.symbol('con_num_l_obs',0);\nvar con_num_debit_amount = S$.symbol('con_num_debit_amount',2);\nvar supp_0 = S$.symbol('supp_0', true)\nvar ucon_num_count = S$.symbol('ucon_num_count', 0)\n\n/* NECESSARY CONRETE TESTS */\nvar i=0;\nfor (i = 0; i < 10; i++){\n  if (ucon_num_h_balance == i) {}\n}\n// var j=0;\n// for (j = 0; j < 4; j++){\n//   if (con_num_debit_amount == j) {}\n// }\n// console.log((ucon_h_balance / con_debit_amount))\n// count = (ucon_h_balance / con_debit_amount)\n/* MAIN JS PROGRAM */\nvar c\nucon_num_count = ucon_num_h_balance/con_num_debit_amount\n// if (ucon_h_balance >= con_debit_amount){\n  // while(ucon_h_balance >= con_debit_amount){\n  // for (c=0; c < ucon_num_count; c++){\n    ucon_num_h_balance = ucon_num_h_balance - con_num_debit_amount;\n    if (!supp_0){\n      con_num_l_obs = con_num_l_obs + 1;\n    }\n  // }\n  // }\n// }\n// console.log(l_obs)\n/* END OF PROGRAM */\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(497, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/test/extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/test/extended.js');
            J$.N(505, 'S$', S$, 0);
            J$.N(513, 'ucon_num_h_balance', ucon_num_h_balance, 0);
            J$.N(521, 'con_num_l_obs', con_num_l_obs, 0);
            J$.N(529, 'con_num_debit_amount', con_num_debit_amount, 0);
            J$.N(537, 'supp_0', supp_0, 0);
            J$.N(545, 'ucon_num_count', ucon_num_count, 0);
            J$.N(553, 'i', i, 0);
            J$.N(561, 'c', c, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_num_h_balance = J$.X1(89, J$.W(81, 'ucon_num_h_balance', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_num_h_balance', 21, false), J$.T(65, 20, 22, false)), ucon_num_h_balance, 3));
            var con_num_l_obs = J$.X1(137, J$.W(129, 'con_num_l_obs', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_num_l_obs', 21, false), J$.T(113, 0, 22, false)), con_num_l_obs, 3));
            var con_num_debit_amount = J$.X1(185, J$.W(177, 'con_num_debit_amount', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_num_debit_amount', 21, false), J$.T(161, 2, 22, false)), con_num_debit_amount, 3));
            var supp_0 = J$.X1(233, J$.W(225, 'supp_0', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_0', 21, false), J$.T(209, true, 23, false)), supp_0, 3));
            var ucon_num_count = J$.X1(281, J$.W(273, 'ucon_num_count', J$.M(265, J$.R(241, 'S$', S$, 1), 'symbol', 0)(J$.T(249, 'ucon_num_count', 21, false), J$.T(257, 0, 22, false)), ucon_num_count, 3));
            var i = J$.X1(305, J$.W(297, 'i', J$.T(289, 0, 22, false), i, 3));
            for (J$.X1(585, i = J$.W(321, 'i', J$.T(313, 0, 22, false), i, 2)); J$.X1(577, J$.C(16, J$.B(10, '<', J$.R(329, 'i', i, 1), J$.T(337, 10, 22, false), 0))); J$.X1(593, J$.B(34, '-', i = J$.W(361, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(353, 'i', i, 1)), J$.T(345, 1, 22, false), 0), i, 2), J$.T(369, 1, 22, false), 0))) {
                if (J$.X1(569, J$.C(8, J$.B(42, '==', J$.R(377, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(385, 'i', i, 1), 0)))) {
                }
            }
            var c;
            J$.X1(417, ucon_num_count = J$.W(409, 'ucon_num_count', J$.B(50, '/', J$.R(393, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(401, 'con_num_debit_amount', con_num_debit_amount, 1), 0), ucon_num_count, 2));
            J$.X1(449, ucon_num_h_balance = J$.W(441, 'ucon_num_h_balance', J$.B(58, '-', J$.R(425, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(433, 'con_num_debit_amount', con_num_debit_amount, 1), 0), ucon_num_h_balance, 2));
            if (J$.X1(601, J$.C(24, J$.U(66, '!', J$.R(457, 'supp_0', supp_0, 1))))) {
                J$.X1(489, con_num_l_obs = J$.W(481, 'con_num_l_obs', J$.B(74, '+', J$.R(465, 'con_num_l_obs', con_num_l_obs, 1), J$.T(473, 1, 22, false), 0), con_num_l_obs, 2));
            }
        } catch (J$e) {
            J$.Ex(609, J$e);
        } finally {
            if (J$.Sr(617)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
