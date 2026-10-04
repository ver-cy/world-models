R4 DELTA INPUT PART 2/8. Continue retaining the exact R3 baseline plus these patches. No tools or audit yet. A file/diff may span parts. ACK only this part number and its end marker.

incipal-collision','changed-content','stale-head','stale-fence'))
 JCOMMAND={'oneOf':[ref('Command'),obj(op=enum('conflict-observation'),body=ref('ConflictRecord'))]}
 D['JournalEvent']=obj(sequence=P,previousDigest=H,actor=U,recordedAt=T,command=JCOMMAND,result=ref('JournalResult'),outcomeDigest=H,digest=H)
-NATIVE=obj(format=enum('vercy-source-sync-journal-snapshot'),version=enum('0.1.0'),buildId=H,config=ref('Bootstrap'),events=arr(ref('JournalEvent'),2000),root=H,resumable=enum(False))
+NATIVE=obj(format=enum('vercy-source-sync-journal-snapshot'),version=enum('0.1.0'),buildId=H,config=ref('Bootstrap'),events=arr(ref('JournalEvent'),128),root=H,resumable=enum(False))
 SCHEMA={'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'urn:vercy:enterprise-source-synchronization:0.1.0:inputs','$defs':D,**NATIVE}
 if __name__=='__main__':
     (Path(__file__).parent/'sync.schema.json').write_text(json.dumps(SCHEMA,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
     print(json.dumps({'definitions':len(D),'commands':len(OPS)}))
--- a/examples/ai-team.json
+++ b/examples/ai-team.json
@@ -1,8 +1,8 @@
 {
   "format": "vercy-source-sync-archive",
   "version": "0.1.0",
-  "buildId": "sha256:90421fd37ea30b8b7fb546c5fffdf3cbf28ef16a6daf487cbc919f5644515287",
+  "buildId": "sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6",
   "config": {
     "admin": "urn:synthetic:admin",
     "dimensionId": "urn:synthetic:company-dimension:ai-team",
     "protectedNamespace": "urn:synthetic:evidence-store",
@@ -26,11 +26,11 @@
           "tenant": "tenant-a"
         },
         "op": "source"
       },
-      "digest": "sha256:bec51728b7b407c051ff549073281485300f005950ddf86cb5ea3a8e4ad4ad5f",
+      "digest": "sha256:0be1d645db706c049754983a65238fde044bbb66483ddf7146e53200f7878ae0",
       "outcomeDigest": "sha256:815b211bfe0c55457128970544a1f1ea38bf9c9ddaa41a82f84fa58112bfcbf1",
-      "previousDigest": "sha256:426aa39d45457076a6a9a8119a27b48ea300c6608420f1befc89c0ae9082400a",
+      "previousDigest": "sha256:b905f99479229282c2d4f1673b4234566eaadee232088ae118ddb1bc243e1187",
       "recordedAt": "2026-01-01T00:00:01Z",
       "result": {
         "status": "recorded"
       },
@@ -79,11 +79,11 @@
           }
         },
         "op": "scope"
       },
-      "digest": "sha256:b9d93199f131a15b6d7b30ace2eb3bfaa244476aca6d3ba57463d684636fdb7f",
+      "digest": "sha256:c50c595b01bcc2945bf2d88471f6f2ec67a08d0ea297f5d8b4c494ad74e9d8ad",
       "outcomeDigest": "sha256:05e0bc38bc267566f9d8ebeae2233c36264442db6dcd9375e058f41f7f8bb488",
-      "previousDigest": "sha256:bec51728b7b407c051ff549073281485300f005950ddf86cb5ea3a8e4ad4ad5f",
+      "previousDigest": "sha256:0be1d645db706c049754983a65238fde044bbb66483ddf7146e53200f7878ae0",
       "recordedAt": "2026-01-01T00:00:02Z",
       "result": {
         "status": "recorded"
       },
@@ -128,11 +128,11 @@
           ]
         },
         "op": "catalogue"
       },
-      "digest": "sha256:38c8a2c38a3066db5c1abfeae41e3f49596a1ea5f3b8eea79eaad96829dd18fb",
+      "digest": "sha256:f98acac5d836f3e38e905dea453d3ce930527db9c857ea0b455010b6bde69642",
       "outcomeDigest": "sha256:e3a0f91d3a07c426957a5b7afe21cc23766e571458407443f2f5ceed8635470d",
-      "previousDigest": "sha256:b9d93199f131a15b6d7b30ace2eb3bfaa244476aca6d3ba57463d684636fdb7f",
+      "previousDigest": "sha256:c50c595b01bcc2945bf2d88471f6f2ec67a08d0ea297f5d8b4c494ad74e9d8ad",
       "recordedAt": "2026-01-01T00:00:03Z",
       "result": {
         "status": "recorded"
       },
@@ -186,11 +186,11 @@
           "revision": 1
         },
         "op": "policy"
       },
-      "digest": "sha256:6d297db11e9c3a13335445776312a5315f97d2748c9876dbde7ac25dfe18044c",
+      "digest": "sha256:f34241c274c9036f06cb297bd1d627ee429b0fc48ddd3a5ffb14c0728a6daeca",
       "outcomeDigest": "sha256:3ddfda364f8e99a81f20476f803909d126146f9e2b20ddd6281cbd8a3615e4f6",
-      "previousDigest": "sha256:38c8a2c38a3066db5c1abfeae41e3f49596a1ea5f3b8eea79eaad96829dd18fb",
+      "previousDigest": "sha256:f98acac5d836f3e38e905dea453d3ce930527db9c857ea0b455010b6bde69642",
       "recordedAt": "2026-01-01T00:00:04Z",
       "result": {
         "status": "recorded"
       },
@@ -211,11 +211,11 @@
           "scopeId": "urn:synthetic:scope"
         },
         "op": "epoch-open"
       },
-      "digest": "sha256:e9727ba11676e0d1969627672c2662ffd41f88d55a96a7cab70b72e1b9585d60",
+      "digest": "sha256:de52c1b67aea2afe71b78bf3ca683e3df822650b0efc2340bb4cddde27332045",
       "outcomeDigest": "sha256:c37c2746668c076bee870a88c10ab584c30e76f648aa435cc84d960bd092f027",
-      "previousDigest": "sha256:6d297db11e9c3a13335445776312a5315f97d2748c9876dbde7ac25dfe18044c",
+      "previousDigest": "sha256:f34241c274c9036f06cb297bd1d627ee429b0fc48ddd3a5ffb14c0728a6daeca",
       "recordedAt": "2026-01-01T00:00:05Z",
       "result": {
         "status": "recorded"
       },
@@ -251,9 +251,9 @@
             "namespace": "urn:synthetic:evidence-store",
             "protection": "restricted",
             "ref": "urn:synthetic:evidence:schema-v1"
           },
-          "scheme": "urn:synthetic:scheme:board-key",
+          "scheme": "urn:synthetic:scheme:dataset-key",
           "schemeVersion": "1",
           "sourceId": "urn:synthetic:source",
           "sourceObjectKind": "dataset-record",
           "sourceQueryProjection": {
@@ -264,11 +264,11 @@
           }
         },
         "op": "scope"
       },
-      "digest": "sha256:25f8f99817060b3463055e8a1a8d2bbf018ea2553cc3522de8a115601812e98b",
-      "outcomeDigest": "sha256:25b515709db6133a4c8ee5a059e44236e1333436a65faa33e47185eceea12e8b",
-      "previousDigest": "sha256:e9727ba11676e0d1969627672c2662ffd41f88d55a96a7cab70b72e1b9585d60",
+      "digest": "sha256:b5c62aea01e780faec4346c63c26f77c0026ce24c45b71f3dc7b016b0b9e8b6c",
+      "outcomeDigest": "sha256:91d937e475fac2ce4d73e392093002007aed0c521adf44ea52d7b6feab815b37",
+      "previousDigest": "sha256:de52c1b67aea2afe71b78bf3ca683e3df822650b0efc2340bb4cddde27332045",
       "recordedAt": "2026-01-01T00:00:06Z",
       "result": {
         "status": "recorded"
       },
@@ -355,11 +355,11 @@
           "revision": 2
         },
         "op": "policy"
       },
-      "digest": "sha256:d25a21851f3d051dda8efe313eb632c0dc7a2613a9654b9b4253d6ea6c4ae918",
-      "outcomeDigest": "sha256:8de1e46d8a78243c6cdefc5cc594de53194bed6a6c248565adb705d1b2a5d959",
-      "previousDigest": "sha256:25f8f99817060b3463055e8a1a8d2bbf018ea2553cc3522de8a115601812e98b",
+      "digest": "sha256:57a5fae9912fc7c331177bc23b2b2bb87157fd3cec22a042fe883ac94cd3c94e",
+      "outcomeDigest": "sha256:361fbee91322923474134f86cafa0f142926af00e33498925e7c1bf6914b2d81",
+      "previousDigest": "sha256:b5c62aea01e780faec4346c63c26f77c0026ce24c45b71f3dc7b016b0b9e8b6c",
       "recordedAt": "2026-01-01T00:00:07Z",
       "result": {
         "status": "recorded"
       },
@@ -380,11 +380,11 @@
           "scopeId": "urn:synthetic:scope:dataset"
         },
         "op": "epoch-open"
       },
-      "digest": "sha256:abb8b9433bcaf1c980731be2a29db0ed69ad20f364f5490c3365bbc7842d40bf",
-      "outcomeDigest": "sha256:048844a4b374933e07d5ad60fe291a86e4636d326d94406f83d83e425da60a74",
-      "previousDigest": "sha256:d25a21851f3d051dda8efe313eb632c0dc7a2613a9654b9b4253d6ea6c4ae918",
+      "digest": "sha256:62b0ccf7221e5ad405491377ce7fbdb46ad6305b0925fe902be68d48ca6b7125",
+      "outcomeDigest": "sha256:d8bda5a59b99998744d621b5763a9266f5a9976dae83a3989cbb042403ba8a9a",
+      "previousDigest": "sha256:57a5fae9912fc7c331177bc23b2b2bb87157fd3cec22a042fe883ac94cd3c94e",
       "recordedAt": "2026-01-01T00:00:08Z",
       "result": {
         "status": "recorded"
       },
@@ -425,11 +425,11 @@
           "validTo": null
         },
         "op": "mapping"
       },
-      "digest": "sha256:83cba03bf678696a20063dfd198e37488c7fe973963cf903ed7ac9457c81f728",
-      "outcomeDigest": "sha256:d9372d63e2ca1821d6cf3df51f59f7e1720e0372824ff4f3299e729e9f68c2df",
-      "previousDigest": "sha256:abb8b9433bcaf1c980731be2a29db0ed69ad20f364f5490c3365bbc7842d40bf",
+      "digest": "sha256:62709051b23233be4a539231eaa6726f191d0417ff12bdcca1a3b484052b89d7",
+      "outcomeDigest": "sha256:f0d8be5cb48286592bba4b4daf37fb9e165b7152c3a862eb0148231c5f9c92ba",
+      "previousDigest": "sha256:62b0ccf7221e5ad405491377ce7fbdb46ad6305b0925fe902be68d48ca6b7125",
       "recordedAt": "2026-01-01T00:00:09Z",
       "result": {
         "status": "recorded"
       },
@@ -445,11 +445,11 @@
           "to": "active"
         },
         "op": "mapping-state"
       },
-      "digest": "sha256:74a813e2eddfcc10751a1bab0be4f4b740aac4c3573ef31971f616a839f51c21",
-      "outcomeDigest": "sha256:e863402b74070af3a784ae2b966433e9fb8dc4b57ef0891a72103f64a59ad82f",
-      "previousDigest": "sha256:83cba03bf678696a20063dfd198e37488c7fe973963cf903ed7ac9457c81f728",
+      "digest": "sha256:28c2c7a2208557f0c5aa973c43b903004ee8f507f60bc6393382536b469371a3",
+      "outcomeDigest": "sha256:da1da281c5bc47f1c6fe2dfc2355e8f3e5f78c1956828be71cd1de6baf412102",
+      "previousDigest": "sha256:62709051b23233be4a539231eaa6726f191d0417ff12bdcca1a3b484052b89d7",
       "recordedAt": "2026-01-01T00:00:10Z",
       "result": {
         "status": "recorded"
       },
@@ -509,11 +509,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:4225e6ae8bb80057a4b66d758e36916e786cf8ae971ac8799da6644c239afcbc",
-      "outcomeDigest": "sha256:c5b20b3249c13f7e368950c4f96ca95d2ebcf5216396051bc403ec7499898c5d",
-      "previousDigest": "sha256:74a813e2eddfcc10751a1bab0be4f4b740aac4c3573ef31971f616a839f51c21",
+      "digest": "sha256:c26db94986847330b29b66591864b4b6ee88ceed615c8b0ed2b98b88827343f5",
+      "outcomeDigest": "sha256:d67adad1bf40c8306fa74f1d4778eba9382d9096e9ccc9360d277d7f77a32d33",
+      "previousDigest": "sha256:28c2c7a2208557f0c5aa973c43b903004ee8f507f60bc6393382536b469371a3",
       "recordedAt": "2026-01-01T00:00:11Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:ai-team:11:receipt",
         "status": "committed"
@@ -574,11 +574,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:2c971675de9bed2f83ed529863381811eb2a04adf5a4f25e4060471c39d389e9",
-      "outcomeDigest": "sha256:b373ec7267acf8b45b43b3bd9996dfdd3df9f53a421b608a98e7a50903872f32",
-      "previousDigest": "sha256:4225e6ae8bb80057a4b66d758e36916e786cf8ae971ac8799da6644c239afcbc",
+      "digest": "sha256:a6d426116598f3c07cc897b2ea1f9537b278908c4d4a29af812d83c5050a8a33",
+      "outcomeDigest": "sha256:b70ce17d7b8dbf95168e17eb2a7834cb86fffbb5bc125e21491f3ab281719bdf",
+      "previousDigest": "sha256:c26db94986847330b29b66591864b4b6ee88ceed615c8b0ed2b98b88827343f5",
       "recordedAt": "2026-01-01T00:00:12Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:ai-team:12:receipt",
         "status": "committed"
@@ -630,11 +630,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:b0274b5b95c9d40987eee7299e36e053c767399665756703d6a3a25c39eb7307",
-      "outcomeDigest": "sha256:0c663f481f3abc6e0eb3ea1ea69e9e70d8c9ebd5ac82c5a67230d598378114fe",
-      "previousDigest": "sha256:2c971675de9bed2f83ed529863381811eb2a04adf5a4f25e4060471c39d389e9",
+      "digest": "sha256:09d9d671679411fe150e2a38d02577bed9f7fd30636367a7bf28d7a208a67e69",
+      "outcomeDigest": "sha256:fda7b0257133e81365375d3db1ca722ccd2b80170ea657bc09adbce1af272aa4",
+      "previousDigest": "sha256:a6d426116598f3c07cc897b2ea1f9537b278908c4d4a29af812d83c5050a8a33",
       "recordedAt": "2026-01-01T00:00:13Z",
       "result": {
         "receiptId": "urn:synthetic:sync-register:ai-team:13:receipt",
         "status": "committed"
@@ -844,9 +844,9 @@
           "namespace": "urn:synthetic:evidence-store",
           "protection": "restricted",
           "ref": "urn:synthetic:evidence:schema-v1"
         },
-        "scheme": "urn:synthetic:scheme:board-key",
+        "scheme": "urn:synthetic:scheme:dataset-key",
         "schemeVersion": "1",
         "sourceId": "urn:synthetic:source",
         "sourceObjectKind": "dataset-record",
         "sourceQueryProjection": {
@@ -854,9 +854,9 @@
           "namespace": "urn:synthetic:evidence-store",
           "protection": "restricted",
           "ref": "urn:synthetic:evidence:query-shape"
         },
-        "fingerprint": "sha256:8ae43ad221a06fe6e27f5213cd8fd578258b2886ab2466da628db3b9f8ac2be8"
+        "fingerprint": "sha256:c6c7cb740e3b1d81296bfe03c069a2221250ce549947c5cd331f8a6c0198e1af"
       }
     },
     "mappings": {
       "urn:synthetic:mapping:1": [
@@ -895,9 +895,9 @@
           "lineage": [
             "urn:synthetic:source",
             "instance-1",
             "datasets",
-            "urn:synthetic:scheme:board-key",
+            "urn:synthetic:scheme:dataset-key",
             "1",
             "d7",
             "record-1"
           ],
@@ -944,9 +944,9 @@
           "lineage": [
             "urn:synthetic:source",
             "instance-1",
             "datasets",
-            "urn:synthetic:scheme:board-key",
+            "urn:synthetic:scheme:dataset-key",
             "1",
             "d7",
             "record-1"
           ],
@@ -1090,9 +1090,9 @@
             "lineage": [
               "urn:synthetic:source",
               "instance-1",
               "datasets",
-              "urn:synthetic:scheme:board-key",
+              "urn:synthetic:scheme:dataset-key",
               "1",
               "d7",
               "record-1"
             ],
@@ -1202,9 +1202,9 @@
             "lineage": [
               "urn:synthetic:source",
               "instance-1",
               "datasets",
-              "urn:synthetic:scheme:board-key",
+              "urn:synthetic:scheme:dataset-key",
               "1",
               "d7",
               "record-2"
             ],
@@ -1304,7 +1304,7 @@
       }
     },
     "conflicts": []
   },
-  "root": "sha256:b0274b5b95c9d40987eee7299e36e053c767399665756703d6a3a25c39eb7307",
+  "root": "sha256:09d9d671679411fe150e2a38d02577bed9f7fd30636367a7bf28d7a208a67e69",
   "resumable": false
 }
--- a/examples/international.json
+++ b/examples/international.json
@@ -1,8 +1,8 @@
 {
   "format": "vercy-source-sync-archive",
   "version": "0.1.0",
-  "buildId": "sha256:90421fd37ea30b8b7fb546c5fffdf3cbf28ef16a6daf487cbc919f5644515287",
+  "buildId": "sha256:b782bbca6c4b5bcc9344dde998d88486c1635ce45a00fbcf6bb7bb179af25cd6",
   "config": {
     "admin": "urn:synthetic:admin",
     "dimensionId": "urn:synthetic:company-dimension:international",
     "protectedNamespace": "urn:synthetic:evidence-store",
@@ -26,11 +26,11 @@
           "tenant": "tenant-a"
         },
         "op": "source"
       },
-      "digest": "sha256:99443a534f1de04b4c004f77b0cfcc2723ae1ba7b068ebea4558937c8ca51a32",
+      "digest": "sha256:bf9dc6c4cc5ddf6d7309fbecc98ab159a8323bfafe331577e7baffc4c52214f5",
       "outcomeDigest": "sha256:bdde571511c9093baf7ed303a6f9d623468dca08cef6895064b3265514ed9f11",
-      "previousDigest": "sha256:6587b92b10cfde5b96f588c9f6a07f436c34551c4029f744c0cdefa31557b038",
+      "previousDigest": "sha256:93e27ab928afb204e5907ebe15e90bfe6af55ec6c79e1ee0fa49f73910ef1b08",
       "recordedAt": "2026-01-01T00:00:01Z",
       "result": {
         "status": "recorded"
       },
@@ -79,11 +79,11 @@
           }
         },
         "op": "scope"
       },
-      "digest": "sha256:987ba2f849f28c4b72b61f09bc990173e4c723582b6047c731edf03c9b0f3087",
+      "digest": "sha256:b324d303ecdd6bba4e48f9d9cde3c338d0c3870238006a3ed304fda94f53d6a2",
       "outcomeDigest": "sha256:1a0f434ce64dba88887e13661bc54bc3ba919fdf9e41a493ed9b53fc2057d14a",
-      "previousDigest": "sha256:99443a534f1de04b4c004f77b0cfcc2723ae1ba7b068ebea4558937c8ca51a32",
+      "previousDigest": "sha256:bf9dc6c4cc5ddf6d7309fbecc98ab159a8323bfafe331577e7baffc4c52214f5",
       "recordedAt": "2026-01-01T00:00:02Z",
       "result": {
         "status": "recorded"
       },
@@ -128,11 +128,11 @@
           ]
         },
         "op": "catalogue"
       },
-      "digest": "sha256:8ec15783383c2c7bdce8b96461a1c91dbec45d90aff349ba95152e6d3d3dd642",
+      "digest": "sha256:dd9f69ab87bac9b8a8984c48ef5db6dfd6266d0424da82cfd4fb7a3dd59de944",
       "outcomeDigest": "sha256:2a2e9d8b3c333a93b63d74eecba35645930374e97101e37a826ff93861e2fcdf",
-      "previousDigest": "sha256:987ba2f849f28c4b72b61f09bc990173e4c723582b6047c731edf03c9b0f3087",
+      "previousDigest": "sha256:b324d303ecdd6bba4e48f9d9cde3c338d0c3870238006a3ed304fda94f53d6a2",
       "recordedAt": "2026-01-01T00:00:03Z",
       "result": {
         "status": "recorded"
       },
@@ -186,11 +186,11 @@
           "revision": 1
         },
         "op": "policy"
       },
-      "digest": "sha256:25c5971a7b0322b1c7a2d9c136aef13f87f1d012a4383fe76bdb10b0d09011ec",
+      "digest": "sha256:ecf32bde903d39836ee9470ef0390a90cc777f02b6659b858e2ac33d1f9fec86",
       "outcomeDigest": "sha256:b838d4f1c71cd0d7ce6856dd6e849a1b75f0870cd3921e0ba8e1d692a874cf94",
-      "previousDigest": "sha256:8ec15783383c2c7bdce8b96461a1c91dbec45d90aff349ba95152e6d3d3dd642",
+      "previousDigest": "sha256:dd9f69ab87bac9b8a8984c48ef5db6dfd6266d0424da82cfd4fb7a3dd59de944",
       "recordedAt": "2026-01-01T00:00:04Z",
       "result": {
         "status": "recorded"
       },
@@ -211,11 +211,11 @@
           "scopeId": "urn:synthetic:scope"
         },
         "op": "epoch-open"
       },
-      "digest": "sha256:025a95f83c6971de237d61e65de5824156ad5c57f0fc730ccdae591bb88dc583",
+      "digest": "sha256:e1c6a0b10cc88cc3439e009fc3fe363e9649e16aa52aac5afebec43cfed0fed8",
       "outcomeDigest": "sha256:26cfb27771c7ec9c6b483f694c52c38a366d0dc61dc190d33012cfcbf956305d",
-      "previousDigest": "sha256:25c5971a7b0322b1c7a2d9c136aef13f87f1d012a4383fe76bdb10b0d09011ec",
+      "previousDigest": "sha256:ecf32bde903d39836ee9470ef0390a90cc777f02b6659b858e2ac33d1f9fec86",
       "recordedAt": "2026-01-01T00:00:05Z",
       "result": {
         "status": "recorded"
       },
@@ -238,11 +238,11 @@
           "tenant": "tenant-b"
         },
         "op": "source"
       },
-      "digest": "sha256:dd38ddbd308555950b6c3e9b7b8308b1f5852a8a2fdf4e309e8a5d4b355125bd",
+      "digest": "sha256:601c4ab9f162afb49d375e83643c797774e89c9b4d3afce5e4bbef537d62016b",
       "outcomeDigest": "sha256:210b086814e5c4016adeb8f2710f98480cd33869dd90a44c9d320e69db147096",
-      "previousDigest": "sha256:025a95f83c6971de237d61e65de5824156ad5c57f0fc730ccdae591bb88dc583",
+      "previousDigest": "sha256:e1c6a0b10cc88cc3439e009fc3fe363e9649e16aa52aac5afebec43cfed0fed8",
       "recordedAt": "2026-01-01T00:00:06Z",
       "result": {
         "status": "recorded"
       },
@@ -291,11 +291,11 @@
           }
         },
         "op": "scope"
       },
-      "digest": "sha256:fed89268df0c7dc283f912471292dccecfb71d225bd5daaa0ed12056a2801aff",
+      "digest": "sha256:e98cc414542e2e208d1376e9770db0a14443d18a21d74a224a0a9a30e4c73592",
       "outcomeDigest": "sha256:c4fb247bcb541ec3a7c3ecb5785b6df2eb92338840ff6e8cda26667a317a1d09",
-      "previousDigest": "sha256:dd38ddbd308555950b6c3e9b7b8308b1f5852a8a2fdf4e309e8a5d4b355125bd",
+      "previousDigest": "sha256:601c4ab9f162afb49d375e83643c797774e89c9b4d3afce5e4bbef537d62016b",
       "recordedAt": "2026-01-01T00:00:07Z",
       "result": {
         "status": "recorded"
       },
@@ -382,11 +382,11 @@
           "revision": 2
         },
         "op": "policy"
       },
-      "digest": "sha256:95a4fe9b13109b7df703311499289596e645d19eba3e079f31caa693ccf2b41e",
+      "digest": "sha256:1ddd89f35a32ac74aa41051d1d6a076da74780c81afac2587d19810bbe091d27",
       "outcomeDigest": "sha256:3b6caf7c35e2bf89e99eb66010a451bd36710255a4b268d608a0c1fc46b48fe1",
-      "previousDigest": "sha256:fed89268df0c7dc283f912471292dccecfb71d225bd5daaa0ed12056a2801aff",
+      "previousDigest": "sha256:e98cc414542e2e208d1376e9770db0a14443d18a21d74a224a0a9a30e4c73592",
       "recordedAt": "2026-01-01T00:00:08Z",
       "result": {
         "status": "recorded"
       },
@@ -407,11 +407,11 @@
           "scopeId": "urn:synthetic:scope:b"
         },
         "op": "epoch-open"
       },
-      "digest": "sha256:ed7f8cfa8256138ce7e6cfbe83c93604394cca52df41b30a24f7cc31ae943b98",
+      "digest": "sha256:810e84232fd980776a1425ec8ba090b123c69fb28fdbcd194a5d3700eb45a499",
       "outcomeDigest": "sha256:f0c6ef5ccde69f41ba499b75fdaa5caf0ce8490200d1db25e077a730a725a13d",
-      "previousDigest": "sha256:95a4fe9b13109b7df703311499289596e645d19eba3e079f31caa693ccf2b41e",
+      "previousDigest": "sha256:1ddd89f35a32ac74aa41051d1d6a076da74780c81afac2587d19810bbe091d27",
       "recordedAt": "2026-01-01T00:00:09Z",
       "result": {
         "status": "recorded"
       },
@@ -452,11 +452,11 @@
           "validTo": null
         },
         "op": "mapping"
       },
-      "digest": "sha256:86a523edf56c57387ae02dc872c40a64aa9ecfad947689b09608a68bc3178e91",
+      "digest": "sha256:cb7f6a90300b7a868360fd3827f4fea60895f6dddfb44ea2de3a4bc25ecee18f",
       "outcomeDigest": "sha256:4b25ddf82a68c9b1ba1ec80c27bbccb0fe66fd2bdce93f532a6085d436cd741a",
-      "previousDigest": "sha256:ed7f8cfa8256138ce7e6cfbe83c93604394cca52df41b30a24f7cc31ae943b98",
+      "previousDigest": "sha256:810e84232fd980776a1425ec8ba090b123c69fb28fdbcd194a5d3700eb45a499",
       "recordedAt": "2026-01-01T00:00:10Z",
       "result": {
         "status": "recorded"
       },
@@ -472,11 +472,11 @@
           "to": "active"
         },
         "op": "mapping-state"
       },
-      "digest": "sha256:6bdbe43a4dcdd368421b0671ec3bb5374014e2cf45097166e1e32a6658139329",
+      "digest": "sha256:5e204aa8cddd082051430afa62d854916529d97b4fb960e0c18ad1540cc2f1a1",
       "outcomeDigest": "sha256:d9fe56ce3930aaf7e463ab17542b2a158ab138d54a1bec88cbff436e52cf36d4",
-      "previousDigest": "sha256:86a523edf56c57387ae02dc872c40a64aa9ecfad947689b09608a68bc3178e91",
+      "previousDigest": "sha256:cb7f6a90300b7a868360fd3827f4fea60895f6dddfb44ea2de3a4bc25ecee18f",
       "recordedAt": "2026-01-01T00:00:11Z",
       "result": {
         "status": "recorded"
       },
@@ -517,11 +517,11 @@
           "validTo": null
         },
         "op": "mapping"
       },
-      "digest": "sha256:a58cd5e5368b0b3f54c6a13028fc0b5a0a7ef5f07dbb83c47de958dc03591415",
+      "digest": "sha256:de246d0802b3be9163e279792a50e7bdaae42fe5641f5d1d07f4a1764bf26905",
       "outcomeDigest": "sha256:11975178afd514c64391ba5a7eddc8668b6e3a596fc207c3166e0cb3477dff09",
-      "previousDigest": "sha256:6bdbe43a4dcdd368421b0671ec3bb5374014e2cf45097166e1e32a6658139329",
+      "previousDigest": "sha256:5e204aa8cddd082051430afa62d854916529d97b4fb960e0c18ad1540cc2f1a1",
       "recordedAt": "2026-01-01T00:00:12Z",
       "result": {
         "status": "recorded"
       },
@@ -537,11 +537,11 @@
           "to": "active"
         },
         "op": "mapping-state"
       },
-      "digest": "sha256:f3c67ad90c7a3a70d4ac9d841189b27c610cf57641600f78795a7631aa0b58d1",
+      "digest": "sha256:0e6b4572b4abb74e1badf99dc8a2165ae7e3720f8bf3e04ca4d61bf080949eb1",
       "outcomeDigest": "sha256:7aeed6f5cfbd20fd6fcbc84851d9da44ceb007ce5b6ee9957fe118d0ff038718",
-      "previousDigest": "sha256:a58cd5e5368b0b3f54c6a13028fc0b5a0a7ef5f07dbb83c47de958dc03591415",
+      "previousDigest": "sha256:de246d0802b3be9163e279792a50e7bdaae42fe5641f5d1d07f4a1764bf26905",
       "recordedAt": "2026-01-01T00:00:13Z",
       "result": {
         "status": "recorded"
       },
@@ -655,11 +655,11 @@
           "fence": 1
         },
         "op": "commit"
       },
-      "digest": "sha256:f903971086a285b686df55c4b1ac2de14c328efe700d6de0f08e8633d3756c45",
+      "digest": "sha256:ae43e2dffa98574dc4928c09964ef7f8dac407faa1f31d8e71788178c12ec137",
       "outcomeDigest": "sha256:3ff796ab7a
END R4 INPUT PART 2/8 â€” SYNC-R4-PART-02
