var app = angular.module("app", [])
    .config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
<<<<<<< HEAD
    .run(function($rootScope) {
    $rootScope.url = 'http://localhost:8000';
    // $rootScope.url = 'http://192.168.1.42:8000';
=======
    .run(function($rootScope, $location) {
    $rootScope.url = $location.$$protocol + '://' + $location.$$host + ':' + $location.$$port;
>>>>>>> origin/master
});