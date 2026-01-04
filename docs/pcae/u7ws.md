# Unit 7 Worksheet

## Instructions

Fill out the worksheet as you progress through the lab and discussions.
Hold your worksheets until the end to turn them in as a final submission packet.

### Resources / Important Links

- <https://sre.google/sre-book/release-engineering/>
- <https://sre.google/workbook/canarying-releases/>
- <https://docs.docker.com/build/building/best-practices/>

#### Downloads

The worksheet has been provided below. The document(s) can be transposed to
the desired format so long as the content is preserved. For example, the `.txt`
could be transposed to a `.md` file.

- <a href="../../assets/pcae/downloads/u7/u7_worksheet.md.txt" target="_blank" download="u7_worksheet.md">:material-download: u7_worksheet.md</a>
- <a href="../../assets/pcae/downloads/u7/u7_worksheet.txt" target="_blank" download>:material-download: u7_worksheet.txt</a>
- <a href="../../assets/pcae/downloads/u7/u7_worksheet.pdf" target="_blank" download>:material-download: u7_worksheet.pdf</a>

### Unit 7 Recording

<img src="../../assets/images/comingsoon.png">
<!-- Playlist: https://www.youtube.com/playlist?list=PLyuZ_vuAWmpoiB5_fo9zXd_leFwzfbA5o -->
<!-- <iframe -->
<!--     style="width: 100%; height: 100%; border: none; -->
<!--     aspect-ratio: 16/9; border-radius: 1rem; background:black" -->
<!--     src="PLACEHOLDER: Unit Embed Link" -->
<!--     title="PLACEHOLDER: Unit recording title" -->
<!--     frameborder="0" -->
<!--     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" -->
<!--     referrerpolicy="strict-origin-when-cross-origin" -->
<!--     allowfullscreen> -->
<!-- </iframe> -->

#### Discussion Post #1

Your infrastructure engineering teams have been experiencing problems re-creating environments. The main problems 
have been around reliably building the exact same environment and also making those builds happen in a timely manner.

Read <https://sre.google/sre-book/release-engineering/> and <https://sre.google/workbook/canarying-releases/> to 
answer the following questions.

1. What is release engineering?
2. What are the release engineering principles?
3. How do the tools we've discussed this week, Apptainer, Packer, Terraform, or even Ansible fit into these topics?

#### Discussion Post #2

Your team is having problems with a deployment. This is the code snippet they are using.

1. What is the provider they are using?
2. How many docker instance are they trying to run, and what are their names?
    a. What ports are they going to be running on?
3. Your team is having problems executing this and have brought it to you. What might
you check, or do with terraform to try to resolve the issue?
    - a. If it’s telling you there are no providers?
    - b. If it’s saying there’s a syntax problem (how can you find it)?
    - c. If there are no resources created?

```terraform linenums="1" title="terraform.tf"
terraform {
	required_providers {
		docker = {
			source = "kreuzwerker/docker"
			version = "~> 2.13.0"
		}
	}
}

provider "docker" {}

resource "docker_image" "nginx" {
	name = "nginx:latest"
	keep_locally = false
}

resource "docker_container" "nginx8080" {
	image = docker_image.nginx.latest
	name = "nginx8080"
	ports {
		internal = 80
		external = 8080
	}
}
resource "docker_container" "nginx8081" {
	image = docker_image.nginx.latest
	name = "nginx8081"
	ports {
		internal = 80
		external = 8081
    }
}
resource "docker_container" "nginx8082" {
	image = docker_image.nginx.latest
	name = "nginx8082"
	ports {
		internal = 80
		external = 8082
	}
}
```

!!! note

    Submit your input by following the link below. The discussion posts are done in Discord Forums.

    - [Link to Discussion Posts](https://discord.com/channels/611027490848374811/1365776270800977962)


## Definitions

- Pipeline

- Inotify-tools

## Digging Deeper

1. What are some of the best practices around container deployments?
<https://docs.docker.com/build/building/best-practices/>

1. Why might we not want to ever run the “latest” tag in production?
2. Why should an application be run as non-root?
3. What is it to be an immutable container?
4. What is it to be a sandboxed container?
    1. What does this mean from the kernel standpoint

## Reflection Questions

1. What questions do you still have about this week?
2. How are you going to use what you've learned in your current role?
