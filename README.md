# Arcaflow Plugin Example Python

## Operation

Download `example.yaml` from this repository.

Run the example.

```shell
cat example.yaml | docker run -i quay.io/arcalot/arcaflow-plugin-example -f -

<!-- Autogenerated documentation by arcaflow-docsgen -->
## Hello world! (`hello-world`)

Says hello :)

### Input

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>InputParams</td></tr>
<tr><th>Properties</th><td><details><summary>name (<code>one of[string]</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>Name</td></tr><tr><th>Description:</th><td>Who do we say hello to?</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Examples (JSON encoded):</th><td>
<pre><code>{&#34;_type&#34;: &#34;fullname&#34;, &#34;first_name&#34;: &#34;Arca&#34;, &#34;last_name&#34;: &#34;Lot&#34;}</code></pre><pre><code>{&#34;_type&#34;: &#34;nickname&#34;, &#34;nick&#34;: &#34;Arcalot&#34;}</code></pre>
</td></tr><tr><th>Type:</th><td><code>one of[string]</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>FullName (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>first_name (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>First name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Examples (JSON encoded):</th><td>
<pre><code>&#34;Arca&#34;</code></pre>
</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr><tr><th>Must match pattern:</th><td><code>^[a-zA-Z]&#43;$</code></td></tr></tbody></table>
        </details><details><summary>last_name (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>Last name</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Examples (JSON encoded):</th><td>
<pre><code>&#34;Lot&#34;</code></pre>
</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr><tr><th>Must match pattern:</th><td><code>^[a-zA-Z]&#43;$</code></td></tr></tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>InputParams (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>name (<code>one of[string]</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>Name</td></tr><tr><th>Description:</th><td>Who do we say hello to?</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Examples (JSON encoded):</th><td>
<pre><code>{&#34;_type&#34;: &#34;fullname&#34;, &#34;first_name&#34;: &#34;Arca&#34;, &#34;last_name&#34;: &#34;Lot&#34;}</code></pre><pre><code>{&#34;_type&#34;: &#34;nickname&#34;, &#34;nick&#34;: &#34;Arcalot&#34;}</code></pre>
</td></tr><tr><th>Type:</th><td><code>one of[string]</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details><details><summary>Nickname (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>nick (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>Nickname</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Examples (JSON encoded):</th><td>
<pre><code>&#34;Arcalot&#34;</code></pre>
</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Minimum length:</th><td>1</td></tr><tr><th>Must match pattern:</th><td><code>^[a-zA-Z]&#43;$</code></td></tr></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

### Outputs


#### error

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>ErrorOutput</td></tr>
<tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>ErrorOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

#### success

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>SuccessOutput</td></tr>
<tr><th>Properties</th><td><details><summary>message (<code>string</code>)</summary>
                <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>SuccessOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>message (<code>string</code>)</summary>
        <table><tbody><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>
<!-- End of autogenerated documentation -->```
