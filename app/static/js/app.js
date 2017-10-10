angular.module('app', [])
  .config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('//').endSymbol('//');
  })
  .controller('MainCtrl', function($scope, $http){
    var self = $scope;
    var apiUrl = '/api/movies';

    self.movies = [];
    self.movie = {};
    self.error = '';

    self.getMovies = function(){
      $http.get(apiUrl).then(function(res){
        console.log(res)
        self.movies = res.data;
      })
    }

    self.create = function(){
      $http.post(apiUrl, self.movie).then(function(res){
        self.getMovies();
        self.movie = '';
        self.error = '';
      }, function(err){
        self.error = err.data.status;
      });
    }

    self.getMovies();
  });
