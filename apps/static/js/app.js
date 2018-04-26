var app = angular.module("app", [])
    .config(function ($interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})
    .directive('ngFiles', ['$parse', function ($parse) {
        function fn_link(scope, element, attrs) {
            var onChange = $parse(attrs.ngFiles);
            element.on('change', function (event) {
                onChange(scope, { $files: event.target.files });
            });
        }
        return {
            link: fn_link
        }
    }
])
    .run(function($rootScope, $location) {
    $rootScope.url = $location.$$protocol + '://' + $location.$$host + ':' + $location.$$port;
})
;