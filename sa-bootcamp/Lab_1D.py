from aws_xray_sdk.core import xray_recorder


print("Start")

# Start a segment
segment = xray_recorder.begin_segment('segment_start')
# Start a subsegment
subsegment = xray_recorder.begin_subsegment('subsegment_task')

# Add metadata and annotations
segment.put_metadata('key', dict, 'namespace')
subsegment.put_annotation('key', 'value')

# Close the subsegment and segment
xray_recorder.end_subsegment()
xray_recorder.end_segment()

print("Done")

