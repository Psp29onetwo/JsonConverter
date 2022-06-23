
# Json converter
## Extracting meaningful json data with python.

**Part #1 : Using Python, convert the above tracker_wise JSON into
frame_wise, as described in the problem statement. Please submit the
complete python code solution.**

> tracker_wise json,
```
{
“rider_info”:{
“frame_id” : {
&lt;rider_details&gt;
}
}
“maker_response” :
{
“video2d” :
{
“data” :
{
“annotations” : [A1, A2, A3 ……… An]
}
}
}
}
```

* Structure of a single tracker element.
```
{
_id : string, # -&gt;This is the tracker_id.
color: rgb(int, int, int) # -&gt; Color of the shape tracked
frames:
{
frame_id1 : annotation1,
frame_id2 : annotation2,
}

}
```

### Problem Statement
The task is to convert **maker_response** -&gt; **video2d**  -&gt; **data**   -&gt;
annotations to **Export_data** -&gt; **annotations** -&gt; **frames**. Use Python to write the
conversion code.

### Details:
● The **maker_response** -&gt;**video2d** -&gt; **data** -&gt; **annotations** -&gt; **frames**
will be a dictionary type element. Each key will represent one
frame_id and all the details associated with it.
● The value of every frame_id in the above mentioned dict will be a
&lt;key : list()&gt; type.
Each element in the list will contain data from all the trackers which
have that frame_id.
Note: The **maker_response** -&gt; **video2d** -&gt; **data** -&gt; **trackers list** can have n
number of trackers. All the trackers should be a part if they are
associated with the frame_id under consideration.

---

**Part#2 : Programmatically using python, create a csv file having the
following structure for the above tracker_wise json.
Please submit the complete python code solution.**


```
| frame_id    | tracking_id | label     |
|             |             |               |
|             |             |               |
|             |             |               |
```
