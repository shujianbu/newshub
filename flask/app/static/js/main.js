
d3.json("static/js/list.json", function(error,listObj) {
	if (error) return console.warn(error);
	
	d3.json("static/js/output_compare.json", function(error,compareObj) {
		// console.log("compare:");
		// console.log(compareObj.compare);

		d3.json("static/js/output_deleted.json", function(error,deletedObj) {
			// console.log("deleted:");
			// console.log(deletedObj.deleted);

			// Step 1: Get newspaper list

			var items = [];
			var siteAdd = [];
			var deletedByPaper = [];
			var compareByPaper = [];
			for (var i = 0; i < listObj.list.length; i++) {
				items[i] = listObj.list[i].Name;
				siteAdd[i] = listObj.list[i].link;
				deletedByPaper[i] = [];
				compareByPaper[i] = [];
			}
			$('#sidebar ul').append('<li>' + items.join('</li><li>') + '</li>');
			$('#sidebar ul li:first-child').addClass('selected');

			// Step 2: Get deleted articles 
			console.log(deletedObj.deleted.length);

			for(var i = 0; i < deletedObj.deleted.length; i++){
				if(siteAdd.indexOf(deletedObj.deleted[i]['domain']) != -1){
					deletedByPaper[ siteAdd.indexOf(deletedObj.deleted[i]['domain']) ].push(deletedObj.deleted[i])
				} else {
					console.log("invalid domain: " + deletedObj.deleted[i]['domain']);
				}
			}

			console.log(deletedByPaper);

			// Step 3: Get compare articles 

			for(var i = 0; i < compareObj.compare.length; i++){
				if(siteAdd.indexOf(compareObj.compare[i]['domain']) != -1){
					compareByPaper[ siteAdd.indexOf(compareObj.compare[i]['domain']) ].push(compareObj.compare[i])
				} else {
					console.log("invalid domain: " + compareObj.compare[i]['domain']);
				}
			}
			console.log(compareByPaper);

			// Step 4: Show default people's daily
			var content = "";
			$('.deletedInfo').html(deletedByPaper[0].length + ' articles deleted!')
			for(var i = 0; i < deletedByPaper[0].length; i++){
				content += "<div class='contentEntry'><div class='contentHead'><div class='title'>Title: " + deletedByPaper[0][i].title + "</div><div class='time_pub'>Time Published: " + deletedByPaper[0][i].time_pub + "</div><div class='time_check'>Time Checked: " + deletedByPaper[0][i].time_check + "</div></div><div class = 'url'><a href='" + deletedByPaper[0][i].url + "' target='_blank'>DELETED</a>" + "</div><div class='deletedContent'>" + deletedByPaper[0][i].content + "</div></div>" 
			}
			$('.deletedDiv').html(content)

			content = "";
			$('.compareInfo').html(compareByPaper[0].length + ' articles modified!')
			for(var i = 0; i < compareByPaper[0].length; i++){
				content += "<div class='contentEntry'><div class='contentHead'><div class='title'>Title: " + compareByPaper[0][i].title + "</div><div class='time_pub'> Time Published: " + compareByPaper[0][i].time_pub + "</div><div class='time_check'>Time Checked: " + compareByPaper[0][i].time_check + "</div></div><div class = 'url'><a href='" + compareByPaper[0][i].url + "' target='_blank'>VIEW</a>" + "</div><div class='compareContent'>" + compareByPaper[0][i].content + "</div></div>" 
			}
			$('.compareDiv').html(content)

			// Step 5: Click Handler
			$('#sidebar ul li').click(function(e) {
				var index = items.indexOf(e.target.innerHTML);
				$('#sidebar ul li').removeClass('selected');
				$('#sidebar ul li').eq(index).addClass('selected');
				$('.page-header small').html(e.target.innerHTML);
				$('.newspaperDesc').html(listObj.list[index].descr);
				
				content = ""; // update delete
				$('.deletedInfo').html(deletedByPaper[index].length + ' articles deleted!')
				for(var i = 0; i < deletedByPaper[index].length; i++){
					content += "<div class='contentEntry'><div class='contentHead'><div class='title'>Title: " + deletedByPaper[index][i].title + "</div><div class='time_pub'>Time Published: " + deletedByPaper[index][i].time_pub + "</div><div class='time_check'>Time Checked: " + deletedByPaper[index][i].time_check + "</div></div><div class = 'url'><a href='" + deletedByPaper[index][i].url + "' target='_blank'>DELETED</a>" + "</div><div class='deletedContent'>" + deletedByPaper[index][i].content + "</div></div>" 
				}
				$('.deletedDiv').html(content)

				content = ""; // update modifited
				$('.compareInfo').html(compareByPaper[index].length + ' articles modified!')
				for(var i = 0; i < compareByPaper[index].length; i++){
					content += "<div class='contentEntry'><div class='contentHead'><div class='title'>Title: " + compareByPaper[index][i].title + "</div><div class='time_pub'> Time Published: " + compareByPaper[index][i].time_pub + "</div><div class='time_check'>Time Checked: " + compareByPaper[index][i].time_check + "</div></div><div class = 'url'><a href='" + compareByPaper[index][i].url + "' target='_blank'>VIEW</a>" + "</div><div class='compareContent'>" + compareByPaper[index][i].content + "</div></div>" 
				}
				$('.compareDiv').html(content)

			});

		});
	});
});

