var app = angular.module("app", [])
    .config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
    .run(function($rootScope) {
    // $rootScope.url = 'http://172.20.10.9:8000';
    $rootScope.url = 'http://192.168.1.42:8000';
});