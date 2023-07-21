var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
        var user = this.dataset.user
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user === 'AnonymousUser'){
			console.log('User is not authenticated')

		}else{
            console.log('uSER IS AUTHENTICATED')
		}
	})
}