J$.iids = {"8":[11,7,11,30],"9":[1,10,1,17],"10":[10,17,10,23],"16":[10,17,10,23],"17":[1,18,1,22],"18":[10,25,10,28],"24":[14,7,14,33],"25":[1,10,1,23],"32":[13,18,13,25],"33":[1,10,1,23],"34":[10,25,10,28],"40":[21,5,21,47],"41":[1,10,1,23],"42":[11,7,11,30],"49":[4,26,4,28],"50":[13,18,13,25],"57":[4,36,4,56],"58":[13,27,13,31],"65":[4,58,4,59],"73":[4,26,4,60],"74":[13,27,13,31],"75":[4,26,4,35],"81":[4,26,4,60],"82":[14,7,14,33],"89":[4,26,4,60],"90":[21,5,21,47],"97":[5,21,5,23],"98":[22,15,22,56],"105":[5,31,5,46],"113":[5,48,5,49],"121":[5,21,5,50],"123":[5,21,5,30],"129":[5,21,5,50],"137":[5,21,5,50],"145":[6,28,6,30],"153":[6,38,6,60],"161":[6,62,6,63],"169":[6,28,6,64],"171":[6,28,6,37],"177":[6,28,6,64],"185":[6,28,6,64],"193":[7,14,7,16],"201":[7,24,7,32],"209":[7,34,7,38],"217":[7,14,7,39],"219":[7,14,7,23],"225":[7,14,7,39],"233":[7,14,7,39],"241":[10,14,10,15],"249":[10,14,10,15],"257":[10,14,10,15],"265":[10,17,10,18],"273":[10,21,10,23],"289":[10,25,10,26],"297":[10,25,10,28],"313":[11,7,11,25],"321":[11,29,11,30],"329":[13,15,13,16],"337":[13,15,13,16],"345":[13,15,13,16],"353":[13,18,13,20],"361":[13,23,13,25],"377":[13,27,13,29],"385":[13,27,13,31],"401":[14,7,14,27],"409":[14,31,14,33],"417":[21,5,21,23],"425":[21,27,21,47],"433":[22,15,22,33],"441":[22,36,22,56],"449":[22,15,22,56],"457":[22,15,22,56],"465":[1,1,33,21],"473":[1,1,33,21],"481":[1,1,33,21],"489":[1,1,33,21],"497":[1,1,33,21],"505":[1,1,33,21],"513":[1,1,33,21],"521":[1,1,33,21],"529":[1,1,33,21],"537":[11,3,11,34],"545":[10,1,12,2],"553":[10,1,12,2],"561":[14,3,14,37],"569":[13,1,15,2],"577":[13,1,15,2],"585":[21,1,31,2],"593":[1,1,33,21],"601":[1,1,33,21],"nBranches":10,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended_jalangi_.js","code":"var S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_num_h_balance = S$.symbol('ucon_num_h_balance', 0);\nvar con_num_l_obs = S$.symbol('con_num_l_obs',0);\nvar con_num_debit_amount = S$.symbol('con_num_debit_amount',0);\nvar supp_0 = S$.symbol('supp_0', true)\n\n/* NECESSARY CONCRETE TESTS */\nfor (var i = 1; i < 10; i++){\n  if (ucon_num_h_balance == i) {}\n}\nfor (let i = 0; i < 10; i++){\n  if (con_num_debit_amount == i) {}\n}\n// console.log((ucon_h_balance / con_debit_amount))\n// con_num_debit_amount = 1\n// ucon_num_h_balance = 1\n// var count = S$.symbol('count',(ucon_h_balance/con_debit_amount))\n/* MAIN JS PROGRAM */\nif (ucon_num_h_balance >= con_num_debit_amount){\n  var count = (ucon_num_h_balance/con_num_debit_amount)\n  // while(ucon_num_h_balance >= con_num_debit_amount){\n  // for (var c = 0; c < count ; c++){\n  //   ucon_num_h_balance = ucon_num_h_balance - con_num_debit_amount;\n  //   if (!supp_0){\n  //     con_num_l_obs = con_num_l_obs + 1;\n  //   }\n  // }\n  // }\n}\n// console.log(l_obs)\n/* END OF PROGRAM */\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(465, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended.js');
            J$.N(473, 'S$', S$, 0);
            J$.N(481, 'ucon_num_h_balance', ucon_num_h_balance, 0);
            J$.N(489, 'con_num_l_obs', con_num_l_obs, 0);
            J$.N(497, 'con_num_debit_amount', con_num_debit_amount, 0);
            J$.N(505, 'supp_0', supp_0, 0);
            J$.N(513, 'i', i, 0);
            J$.N(521, '_i', _i, 0);
            J$.N(529, 'count', count, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_num_h_balance = J$.X1(89, J$.W(81, 'ucon_num_h_balance', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_num_h_balance', 21, false), J$.T(65, 0, 22, false)), ucon_num_h_balance, 3));
            var con_num_l_obs = J$.X1(137, J$.W(129, 'con_num_l_obs', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_num_l_obs', 21, false), J$.T(113, 0, 22, false)), con_num_l_obs, 3));
            var con_num_debit_amount = J$.X1(185, J$.W(177, 'con_num_debit_amount', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_num_debit_amount', 21, false), J$.T(161, 0, 22, false)), con_num_debit_amount, 3));
            var supp_0 = J$.X1(233, J$.W(225, 'supp_0', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_0', 21, false), J$.T(209, true, 23, false)), supp_0, 3));
            for (var i = J$.X1(257, J$.W(249, 'i', J$.T(241, 1, 22, false), i, 3)); J$.X1(545, J$.C(16, J$.B(10, '<', J$.R(265, 'i', i, 1), J$.T(273, 10, 22, false), 0))); J$.X1(553, J$.B(34, '-', i = J$.W(297, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(289, 'i', i, 1)), J$.T(281, 1, 22, false), 0), i, 2), J$.T(305, 1, 22, false), 0))) {
                if (J$.X1(537, J$.C(8, J$.B(42, '==', J$.R(313, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(321, 'i', i, 1), 0)))) {
                }
            }
            for (var _i = J$.X1(345, J$.W(337, '_i', J$.T(329, 0, 22, false), _i, 3)); J$.X1(569, J$.C(32, J$.B(50, '<', J$.R(353, '_i', _i, 1), J$.T(361, 10, 22, false), 0))); J$.X1(577, J$.B(74, '-', _i = J$.W(385, '_i', J$.B(66, '+', J$.U(58, '+', J$.R(377, '_i', _i, 1)), J$.T(369, 1, 22, false), 0), _i, 2), J$.T(393, 1, 22, false), 0))) {
                if (J$.X1(561, J$.C(24, J$.B(82, '==', J$.R(401, 'con_num_debit_amount', con_num_debit_amount, 1), J$.R(409, '_i', _i, 1), 0)))) {
                }
            }
            if (J$.X1(585, J$.C(40, J$.B(90, '>=', J$.R(417, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(425, 'con_num_debit_amount', con_num_debit_amount, 1), 0)))) {
                var count = J$.X1(457, J$.W(449, 'count', J$.B(98, '/', J$.R(433, 'ucon_num_h_balance', ucon_num_h_balance, 1), J$.R(441, 'con_num_debit_amount', con_num_debit_amount, 1), 0), count, 3));
            }
        } catch (J$e) {
            J$.Ex(593, J$e);
        } finally {
            if (J$.Sr(601)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
