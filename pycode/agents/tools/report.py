# The purpose of this tool is to make ChatGPT write an HTML
# report in a more presentable and sharable format

# StructuredTool instead of simply Tool whenever we have
# multiple arguments to work with. Such as in this case we have
# a filename and its format html
from langchain.tools import StructuredTool

# [JUAI:] Definitely ask the co-pilot about the details around
# pydantic import and how it helps modify the how the
# langchain's source code behaves w.r.t communicating with
# ChatGPT
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w') as f:
        f.write(html)

# Here WriteReportArgsSchema extends the BaseModel
# [JUAI] How it actually affects source modification?
class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str

write_report_tool = StructuredTool.from_function(
        name="write_report",
        description="Write an HTML file to disk. Use this tool whenever a user asks for a report.",
        func=write_report,
        args_schema=WriteReportArgsSchema
        )
