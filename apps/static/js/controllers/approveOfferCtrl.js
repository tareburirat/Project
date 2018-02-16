app.controller('approveOfferCtrl', function ($scope, $http, $rootScope) {
    $scope.mama = $rootScope.url;
    $scope.offers = [];

    $scope.getId = function (id) {
        $scope.id = id;
        getOffer();
    };

    var getOffer = function () {

        var data = {
            seller_id: $scope.id
        };
        $http.post($scope.mama + '/api/high_offers/', data).then(
            function (response) {
                $scope.offers = response.data.offers;
            },
            function () {
                alert('call offer fail')
            }
        )

    };

    $scope.acceptOffer = function (productId, offerId) {
        var data = {
            product_id: productId,
            offer_id: offerId,
            offer_accepted: true
        };
        $http.post($scope.mama + '/api/update_offers/', data).then(
            function () {
                var offerPositionInArray = $scope.offers.find(
                    function (offer) {
                        return offer.id === offerId;
                    }
                );
                $scope.offers.splice(offerPositionInArray, 1)
            },
            function () {
                alert('fail')
            }
        )

    };

    $scope.rejectOffer = function (productId, offerId) {
        var data = {
            product_id: productId,
            offer_accepted: false
        };
        $http.post($scope.mama + '/api/update_offers/', data).then(
            function () {
                var offerPositionInArray = $scope.offers.find(
                    function (offer) {
                        return offer.id === offerId;
                    }
                );
                $scope.offers.splice(offerPositionInArray, 1)
            },
            function () {
                alert('fail1');
            }
        )

    };


});