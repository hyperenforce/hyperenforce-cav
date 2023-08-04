J$.iids = {"8":[11,7,11,26],"9":[1,10,1,17],"10":[10,17,10,23],"16":[10,17,10,23],"17":[1,18,1,22],"18":[10,25,10,28],"24":[26,5,26,12],"25":[1,10,1,23],"33":[1,10,1,23],"34":[10,25,10,28],"41":[1,10,1,23],"42":[11,7,11,26],"49":[4,22,4,24],"50":[18,32,18,65],"57":[4,32,4,48],"58":[25,18,25,51],"65":[4,50,4,52],"66":[26,5,26,12],"73":[4,22,4,53],"74":[27,15,27,28],"75":[4,22,4,31],"81":[4,22,4,53],"89":[4,22,4,53],"97":[5,17,5,19],"105":[5,27,5,38],"113":[5,40,5,41],"121":[5,17,5,42],"123":[5,17,5,26],"129":[5,17,5,42],"137":[5,17,5,42],"145":[6,24,6,26],"153":[6,34,6,52],"161":[6,54,6,55],"169":[6,24,6,56],"171":[6,24,6,33],"177":[6,24,6,56],"185":[6,24,6,56],"193":[7,14,7,16],"201":[7,24,7,32],"209":[7,34,7,38],"217":[7,14,7,39],"219":[7,14,7,23],"225":[7,14,7,39],"233":[7,14,7,39],"241":[10,14,10,15],"249":[10,14,10,15],"257":[10,14,10,15],"265":[10,17,10,18],"273":[10,21,10,23],"289":[10,25,10,26],"297":[10,25,10,28],"313":[11,7,11,21],"321":[11,25,11,26],"329":[18,13,18,15],"337":[18,23,18,30],"345":[18,32,18,46],"353":[18,49,18,65],"361":[18,13,18,66],"363":[18,13,18,22],"369":[18,13,18,66],"377":[18,13,18,66],"385":[25,18,25,32],"393":[25,35,25,51],"401":[25,18,25,51],"409":[25,1,25,52],"417":[26,6,26,12],"425":[27,15,27,24],"433":[27,27,27,28],"441":[27,15,27,28],"449":[27,3,27,29],"457":[1,1,33,21],"465":[1,1,33,21],"473":[1,1,33,21],"481":[1,1,33,21],"489":[1,1,33,21],"497":[1,1,33,21],"505":[1,1,33,21],"513":[1,1,33,21],"521":[11,3,11,30],"529":[10,1,12,2],"537":[10,1,12,2],"545":[26,1,28,2],"553":[1,1,33,21],"561":[1,1,33,21],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended_jalangi_.js","code":"var S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_h_balance = S$.symbol('ucon_h_balance', 10);\nvar con_l_obs = S$.symbol('con_l_obs',0);\nvar con_debit_amount = S$.symbol('con_debit_amount',1);\nvar supp_0 = S$.symbol('supp_0', true)\n\n/* NECESSARY CONCRETE TESTS */\nfor (let i = 1; i < 10; i++){\n  if (ucon_h_balance == i) {}\n}\n// for (let i = 0; i < 10; i++){\n//   if (con_debit_amount == i) {}\n// }\n// console.log((ucon_h_balance / con_debit_amount))\n\nvar count = S$.symbol('count',(ucon_h_balance/con_debit_amount))\n\n/* MAIN JS PROGRAM */\n// if (ucon_h_balance >= con_debit_amount){\n  // var count = (ucon_h_balance/con_debit_amount)\n  // while(ucon_h_balance >= con_debit_amount){\n  // for (var c = 0; c < count ; c++)\n    ucon_h_balance = ucon_h_balance - con_debit_amount;\n    if (!supp_0){\n      con_l_obs = con_l_obs + 1;\n    }\n  // }\n  // }\n// }\n// console.log(l_obs)\n/* END OF PROGRAM */\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(457, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/benchmarks/deniability/wallet_extended.js');
            J$.N(465, 'S$', S$, 0);
            J$.N(473, 'ucon_h_balance', ucon_h_balance, 0);
            J$.N(481, 'con_l_obs', con_l_obs, 0);
            J$.N(489, 'con_debit_amount', con_debit_amount, 0);
            J$.N(497, 'supp_0', supp_0, 0);
            J$.N(505, 'i', i, 0);
            J$.N(513, 'count', count, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_h_balance = J$.X1(89, J$.W(81, 'ucon_h_balance', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_h_balance', 21, false), J$.T(65, 10, 22, false)), ucon_h_balance, 3));
            var con_l_obs = J$.X1(137, J$.W(129, 'con_l_obs', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'con_l_obs', 21, false), J$.T(113, 0, 22, false)), con_l_obs, 3));
            var con_debit_amount = J$.X1(185, J$.W(177, 'con_debit_amount', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_debit_amount', 21, false), J$.T(161, 1, 22, false)), con_debit_amount, 3));
            var supp_0 = J$.X1(233, J$.W(225, 'supp_0', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_0', 21, false), J$.T(209, true, 23, false)), supp_0, 3));
            for (var i = J$.X1(257, J$.W(249, 'i', J$.T(241, 1, 22, false), i, 3)); J$.X1(529, J$.C(16, J$.B(10, '<', J$.R(265, 'i', i, 1), J$.T(273, 10, 22, false), 0))); J$.X1(537, J$.B(34, '-', i = J$.W(297, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(289, 'i', i, 1)), J$.T(281, 1, 22, false), 0), i, 2), J$.T(305, 1, 22, false), 0))) {
                if (J$.X1(521, J$.C(8, J$.B(42, '==', J$.R(313, 'ucon_h_balance', ucon_h_balance, 1), J$.R(321, 'i', i, 1), 0)))) {
                }
            }
            var count = J$.X1(377, J$.W(369, 'count', J$.M(361, J$.R(329, 'S$', S$, 1), 'symbol', 0)(J$.T(337, 'count', 21, false), J$.B(50, '/', J$.R(345, 'ucon_h_balance', ucon_h_balance, 1), J$.R(353, 'con_debit_amount', con_debit_amount, 1), 0)), count, 3));
            J$.X1(409, ucon_h_balance = J$.W(401, 'ucon_h_balance', J$.B(58, '-', J$.R(385, 'ucon_h_balance', ucon_h_balance, 1), J$.R(393, 'con_debit_amount', con_debit_amount, 1), 0), ucon_h_balance, 2));
            if (J$.X1(545, J$.C(24, J$.U(66, '!', J$.R(417, 'supp_0', supp_0, 1))))) {
                J$.X1(449, con_l_obs = J$.W(441, 'con_l_obs', J$.B(74, '+', J$.R(425, 'con_l_obs', con_l_obs, 1), J$.T(433, 1, 22, false), 0), con_l_obs, 2));
            }
        } catch (J$e) {
            J$.Ex(553, J$e);
        } finally {
            if (J$.Sr(561)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
