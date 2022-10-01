J$.iids = {"8":[10,17,10,24],"9":[6,11,6,12],"10":[10,17,10,24],"17":[6,11,6,12],"18":[10,26,10,29],"25":[6,11,6,12],"33":[10,14,10,15],"34":[10,26,10,29],"41":[10,14,10,15],"42":[11,12,11,13],"49":[10,14,10,15],"57":[10,17,10,18],"65":[10,22,10,24],"81":[10,26,10,27],"89":[10,26,10,29],"105":[11,12,11,13],"113":[11,5,11,8],"121":[11,5,11,13],"129":[11,5,11,14],"137":[1,1,14,52],"145":[1,1,14,52],"153":[1,1,14,52],"161":[10,1,12,2],"169":[10,1,12,2],"177":[1,1,14,52],"185":[1,1,14,52],"nBranches":2,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/sum.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/sum_jalangi_.js","code":"// program to display the sum of natural numbers\n\n// take input from the user\n// const number = parseInt(prompt('Enter a positive integer: '));\n\nlet sum = 0;\n\n// looping from i = 1 to number\n// in each iteration, i is increased by 1\nfor (let i = 1; i <= 10; i++) {\n    sum += i;\n}\n\n// console.log('The sum of natural numbers:', sum);\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(137, '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/sum_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/sum.js');
            J$.N(145, 'sum', sum, 0);
            J$.N(153, 'i', i, 0);
            var sum = J$.X1(25, J$.W(17, 'sum', J$.T(9, 0, 22, false), sum, 3));
            for (var i = J$.X1(49, J$.W(41, 'i', J$.T(33, 1, 22, false), i, 3)); J$.X1(161, J$.C(8, J$.B(10, '<=', J$.R(57, 'i', i, 1), J$.T(65, 10, 22, false), 0))); J$.X1(169, J$.B(34, '-', i = J$.W(89, 'i', J$.B(26, '+', J$.U(18, '+', J$.R(81, 'i', i, 1)), J$.T(73, 1, 22, false), 0), i, 2), J$.T(97, 1, 22, false), 0))) {
                J$.X1(129, sum = J$.W(121, 'sum', J$.B(42, '+', J$.R(113, 'sum', sum, 1), J$.R(105, 'i', i, 1), 0), sum, 2));
            }
        } catch (J$e) {
            J$.Ex(177, J$e);
        } finally {
            if (J$.Sr(185)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
