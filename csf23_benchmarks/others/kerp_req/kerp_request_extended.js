var S$ = require('S$');

var con_kerb_request = S$.symbol('kerb_request', true);
// var con_username = S$.symbol('username', true);
// var con_password = S$.symbol('password', true);
// var callback = S$.symbol('callback', true);

// kinit(username, password, callback)

var suppose = require('suppose')
   , exec = require('child_process').exec;

// function kerb_request(username, password, url, callback) {
   kinit(username, password, function() {
      curl(url, function(output) {
         kdestroy(function() {
            callback(output);
         })
      });
   });
// }


function kinit(username, password, callback) {
   suppose('kinit', [ username ])
      .on('Password for ' + username + ': ').respond(password + '\n')
      .end(function(code) {
         callback(code)
      });
}


function curl(url, callback) {
   exec('curl -f -s -S --negotiate -u : ' + url, function(err, stdout, stderr){
      if (err) {
         console.log('Error: ' + err);
      } else {
         callback(stdout);
      }
   });
}

function kdestroy(callback) {
   exec('kdestroy', function(err, stdout, stderr){
      if (err) {
         console.log('Error: ' + err);
      } else {
         callback(stdout);
      }
   });
}
/// END OF FILE ///

// module.exports = kerb_request;
