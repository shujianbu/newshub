d3.json("static/js/list.json", function(error,listObj) {
	if (error) return console.warn(error);

	d3.json("static/js/cn_withcontent.json", function(error,deletedObj) {

		// Step 1: Get newspaper list
		var items = [];
		var siteAdd = [];
		var deletedByPaper = [];
		var deletedData = [];
		var deletedText = [];
		for (var i = 0; i < listObj.list.length; i++) {
			items[i] = listObj.list[i].Name;
			siteAdd[i] = listObj.list[i].link;
			deletedByPaper[i] = [];
			deletedData[i] = {};
			deletedText[i] = {};
			deletedData[i]['Paper'] = listObj.list[i].Name;
			deletedText[i]['Paper'] = listObj.list[i].Name;
			deletedText[i]['Content'] = '';
		}
		$('#sidebar ul').append('<li>' + items.join('</li><li>') + '</li>');
		$('#sidebar ul li:first-child').addClass('selected');

		// Step 2: Get deleted articles 
		// console.log(deletedObj.deleted);

		var startMonth = 201612;
		var endMonth = 201201;
		for(var i = 0; i < deletedObj.deleted.length; i++){
			if(siteAdd.indexOf(deletedObj.deleted[i]['domain']) != -1){
				deletedByPaper[ siteAdd.indexOf(deletedObj.deleted[i]['domain']) ].push(deletedObj.deleted[i]);
				var tmpMonth = deletedObj.deleted[i].time_pub.substring(0,7); // month
				var tmpMonthVal = parseInt(deletedObj.deleted[i].time_pub.substring(0,4)) * 100 + parseInt(deletedObj.deleted[i].time_pub.substring(5,7));
				startMonth = Math.min(startMonth, tmpMonthVal);
				endMonth = Math.max(endMonth, tmpMonthVal);
				if(tmpMonth in deletedData[siteAdd.indexOf(deletedObj.deleted[i]['domain'])])
					deletedData[siteAdd.indexOf(deletedObj.deleted[i]['domain'])][tmpMonth] += 1;
				else
					deletedData[siteAdd.indexOf(deletedObj.deleted[i]['domain'])][tmpMonth] = 1
				deletedText[siteAdd.indexOf(deletedObj.deleted[i]['domain'])]['Content'] += deletedObj.deleted[i].content;
			} else {
				// console.log("invalid domain: " + deletedObj.deleted[i]['domain']);
			}
		}

		var margin = {top: 20, right: 20, bottom: 130, left: 100},
		    width = 1100 - margin.left - margin.right,
		    height = 500 - margin.top - margin.bottom;

		var x = d3.scale.ordinal()
		    .rangeRoundBands([0, width], .1);

		var y = d3.scale.linear()
		    .rangeRound([height, 0]);

		var color = d3.scale.ordinal()
		    .range(["#277c7f", "#ed6c3c", "#f7c052", "#9eabd5", "#f5574c", "#adc691", "#7bb0b2", "#f4a995"]);

		var yAxis = d3.svg.axis()
		    .scale(y)
		    .orient("left");

		var svg = d3.select("#vizBar").append("svg")
		    .attr("width", width + margin.left + margin.right)
		    .attr("height", height + margin.top + margin.bottom)
		  .append("g")
		    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

		var colorRanges = [];
		for(var i = startMonth; i <= endMonth; i++){
			var str = String(i);
			colorRanges.push(str.substring(0,4) + "-" + str.substring(4,6));
		}

		color.domain(colorRanges);
		deletedData.forEach(function(d) {
		    var y0 = 0;
		    d.count = color.domain().map(function(name) { return {name: name, y0: y0, y1: y0 += +d[name]}; });
		    d.total = d.count[d.count.length - 1].y1;
		});

		// deletedData.sort(function(a, b) { return b.total - a.total; });
		// console.log(deletedData);

		x.domain(deletedData.map(function(d) { return d.Paper; }));
		y.domain([0, d3.max(deletedData, function(d) { return d.total; })]);

		var label = svg.selectAll('text')
			.data( x.domain() )
		.enter().append('text')
			.text( function(d,i) {return d;} )
			.attr('x', 0)
			.attr('y', 0)
			.attr('text-anchor', 'end')
			.attr("font-size", "10px")
			.attr('fill', '#444')
			.attr('transform', function(d,i) {return "translate(" + (x.rangeBand() * i + x.rangeBand() ) + ", " + (height + 15) + ")rotate(-45)";})

		svg.append('line')
			.attr('x2', width - margin.left - margin.right)
			.attr('y1', height)
			.attr('y2', height)
			.style("stroke", "#000" );

		svg.append("g")
		    .attr("class", "y axis")
		    .call(yAxis)
		    .append("text")
		    .attr("transform", "rotate(-90)")
		    .attr("y", 6)
		    .attr("dy", ".71em")
		    .style("text-anchor", "end")
		    .text("Deleted Articles");

		var Paper = svg.selectAll(".Paper")
		    .data(deletedData)
		  .enter().append("g")
		    .attr("class", "g")
		    .attr("transform", function(d) { return "translate(" + x(d.Paper) + ",0)"; });

		Paper.selectAll("rect")
		    .data(function(d) { return d.count; })
		    .enter().append("rect")
		    .attr("width", x.rangeBand())
		    .attr("y", function(d) { if(!isNaN(y(d.y1))) return y(d.y1); })
		    .attr("height", function(d) { if(!isNaN(y(d.y1))) return y(d.y0) - y(d.y1); })
		    .style("fill", function(d) { return color(d.name); });

		var legend = svg.selectAll(".legend")
		    .data(color.domain().slice().reverse())
		    .enter().append("g")
		    .attr("class", "legend")
		    .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

		  legend.append("rect")
		    .attr("x", width - 18)
		    .attr("width", 18)
		    .attr("height", 18)
		    .style("fill", color);

		  legend.append("text")
		    .attr("x", width - 24)
		    .attr("y", 9)
		    .attr("dy", ".35em")
		    .style("text-anchor", "end")
		    .text(function(d) { return d; });


		// Step 4: Show default people's daily
	

		// Step 5: Click Handler

		// console.log(deletedByPaper); // each visualization for paper

		$('#sidebar ul li').click(function(e) {
			var index = items.indexOf(e.target.innerHTML);
			$('#sidebar ul li').removeClass('selected');
			$('#sidebar ul li').eq(index).addClass('selected');
			$('.page-header small').html(e.target.innerHTML);
			$('.newspaperDesc').html(listObj.list[index].descr);
			
			content = ""; // update delete
			$('.paperViz').html(deletedByPaper[index].length + ' articles deleted!');

		});


		// Step 6: Textual Analysis
		console.log("deletedText: ");
		console.log(deletedText);
		
		// 字典
		var dict  = [];
		var stop  = {
			"的" : 1,
			"了": 1,
			"和": 1,
			"是": 1,
			"就": 1,
			"都": 1,
			"而": 1,
			"及": 1,
			"与": 1,
			"着": 1,
			"或": 1,
			"一个": 1,
			"沒有": 1,
			"我们": 1,
			"你们": 1,
			"他们": 1,
			"是否": 1
		};

		d3.csv("static/js/dict.csv", function(error,dictCSV) {
			for(var i = 0; i < dictCSV.length; i++){
				dict.push(dictCSV[i].word);
			}
			// console.log(dict);
			var trie = new Trie();
			trie.init(dict);
			// var wordsTest = deletedText[0].Content.substring(0,99);
			var result = trie.splitWords(wordsTest);	
			console.log("分词结果:       ", result);

		});		

	});
});



