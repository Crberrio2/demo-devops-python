# Evidencia de ejecución del pipeline

Pipeline público: https://github.com/Crberrio2/demo-devops-python/actions

Ejecución exitosa (run `27927033050`): los tres jobs en verde.

| Job | Resultado |
|-----|-----------|
| Build, Test, Static Analysis & Coverage | success |
| Docker Build, Scan & Push | success |
| Deploy to Kubernetes (kind) | success |

## Despliegue en Kubernetes (salida real del job `deploy`)

```
configmap/demo-devops-python-config created
secret/demo-devops-python-secret created
service/demo-devops-python created
persistentvolumeclaim/demo-devops-python-data created
deployment.apps/demo-devops-python created
horizontalpodautoscaler.autoscaling/demo-devops-python created
ingress.networking.k8s.io/demo-devops-python created

pod/demo-devops-python-6f668bbdd5-l6pj4   1/1     Running   0   16s
pod/demo-devops-python-6f668bbdd5-s7wcl   1/1     Running   0   16s
service/demo-devops-python   ClusterIP   10.96.156.118   <none>   80/TCP   16s
deployment.apps/demo-devops-python   2/2   2   2   16s
replicaset.apps/demo-devops-python-6f668bbdd5   2   2   2   16s
horizontalpodautoscaler.autoscaling/demo-devops-python   Deployment/demo-devops-python   2   5   2   16s
ingress.networking.k8s.io/demo-devops-python   nginx   demo-devops.local   80   16s
persistentvolumeclaim/demo-devops-python-data   Bound   pvc-...   1Gi   RWO   standard
```

## Smoke tests

```
# Vía Service (port-forward)
GET /api/health/live/  -> {"status":"ok"}

# Vía Ingress (Host: demo-devops.local)
GET /api/health/live/  -> {"status":"ok"}
ingress OK
```

> Para incluir capturas de pantalla, agregar las imágenes en esta carpeta `docs/`
> y referenciarlas aquí. La evidencia anterior proviene directamente de los logs
> públicos del pipeline.
