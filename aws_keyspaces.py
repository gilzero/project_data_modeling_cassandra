# https://docs.aws.amazon.com/keyspaces/latest/devguide/using_python_driver.html
# https://ca-central-1.console.aws.amazon.com/keyspaces/home?region=ca-central-1#getting-started

from cassandra.cluster import Cluster
from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

ssl_context = SSLContext(PROTOCOL_TLSv1_2)
ssl_context.load_verify_locations('/Users/apple/sf-class2-root.crt')
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username='testuser-at-565072184392', password='+EnSYtkEtQ0X03xzKPH9my1edjUKXZMJoUCzKt/hTzs=')
cluster = Cluster(['cassandra.ap-east-1.amazonaws.com'], ssl_context=ssl_context, auth_provider=auth_provider, port=9142)
session = cluster.connect()
# r = session.execute('select * from system_schema.keyspaces')
# print(r.current_rows)

r = session.execute('SELECT * FROM tutorialkeyspace.tutorialtable;')
print(r.current_rows)

session.shutdown()