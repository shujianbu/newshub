
d3.json("static/js/list_cn.json", function(error,listObj) {
	if (error) return console.warn(error);
	
	d3.json("static/js/output_compare.json", function(error,compareObj) {
		console.log("compare:");
		console.log(compareObj.compare);

		d3.json("static/js/output_deleted.json", function(error,deletedObj) {
			console.log("deleted:");
			console.log(deletedObj.deleted);

			// Step 1: Get newspaper list

			var items = [];
			var siteAdd = [];
			var deletedByPaper = {};
			for (var i = 0; i < listObj.list.length; i++) {
				items[i] = listObj.list[i].Name;
				siteAdd[i] = listObj.list[i].link;
			}
			$('#sidebar ul').append('<li>' + items.join('</li><li>') + '</li>');
			$('#sidebar ul li:first-child').addClass('selected');

			$('#sidebar ul li').click(function(e) {
				var index = items.indexOf(e.target.innerHTML);
				$('#sidebar ul li').removeClass('selected');
				$('#sidebar ul li').eq(index).addClass('selected');
				$('.page-header small').html(e.target.innerHTML);
				$('.newspaperDesc').html(listObj.list[index].descr);
			});

			// Step 2: Get deleted articles 
			console.log(deletedObj.deleted.length);
			for(var i = 0; i < deletedObj.deleted.length; i++){
				if(deletedObj.deleted[i]['domain'] == siteAdd[0]) {
					console.log("people");
				} else {
					console.log("other");
				}
			}

			// Step 3: Get compare articles 


		});
	});
});

