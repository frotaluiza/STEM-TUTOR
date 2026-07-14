import SessionViewer from "@/components/pm/SessionViewer";

export default async function SessionViewerPage(props: { params: Promise<{ slug: string }> }) {
  const { slug } = await props.params;
  return <SessionViewer slug={slug} />;
}
